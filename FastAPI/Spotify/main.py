import io
from pyunsplash import PyUnsplash
from io import BytesIO
from PIL import Image, ImageTk
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4
import requests
import os
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import random_photo


from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

app = FastAPI()


class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False


tasks = [
    {
        "id": "9bc6e3d5-9a06-4019-8f36-becdf2908f88",
        "title": "my title",
        "description": "my description",
        "completed": False
    }]


@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task


@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, task_update: Task):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(
                update=task_update.dict(exclude_unset=True))
            tasks[idx] = updated_task
            return updated_task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: UUID):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(idx)

    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/unsplash/random")
def generate_image():
    import requests


# create the main window
root = tk.Tk()
root.title("Image Generator")
root.geometry("700x500")
root.config(bg="white")
root.resizable(False, False)
style = Style(theme="sandstone")

# define a function to retrieve and display an image based on the selected category


def display_image(category):
    key = os.getenv("UNSPLASH_ACCESS_KEY")
    url = f"https://api.unsplash.com/photos/random?query={
        category}&orientation=landscape&client_id={key}"
    # make a request to the Unsplash API to get a random image
    url = f"https://api.unsplash.com/photos/random?query={
        category}&orientation=landscape&client_id={key}"
    data = requests.get(url).json()
    img_data = requests.get(data["urls"]["regular"]).content

    photo = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize(
        (600, 400), resample=Image.LANCZOS))
    label.config(image=photo)
    label.image = photo

# function to enable/disable the "Generate Image" button


def enable_button(*args):
    generate_button.config(state="normal" if category_var.get()
                           != "Choose Category" else "disabled")

# create the GUI elements


def create_gui():
    global category_var, generate_button, label

    # create a dropdown menu for selecting the category
    category_var = tk.StringVar(value="Choose Category")
    category_options = ["Choose Category", "Food", "Animals",
                        "People", "Music", "Art", "Vehicles", "Random"]
    category_dropdown = ttk.OptionMenu(
        root, category_var, *category_options, command=enable_button)
    category_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    category_dropdown.config(width=14)

    # create a button for generating the image
    generate_button = ttk.Button(
        text="Generate Image", state="disabled", command=lambda: display_image(category_var.get()))
    generate_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    label = tk.Label(root, background="white")
    label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # make the columns/rows expandable
    root.columnconfigure([0, 1], weight=1)
    root.rowconfigure(1, weight=1)
    root.mainloop()


create_gui()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
