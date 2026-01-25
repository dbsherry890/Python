#route_homepage.py

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from enum import Enum


templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.get("/")
async def home(request: Request):
	return templates.TemplateResponse("pages/homepage.html",{"request":request})
	
@general_pages_router.get("/") # declaring root route
async def root():
  return {"message": "yuh world"}

@general_pages_router.get("/users")
def get_users(page_size: int=3, page_number: int=1):
  return {
      "users": [
        {"user_id": 1}, 
        {"user_id": 2},
        {"user_id": 3},
        {"user_id": 4}
      ]
  }

@general_pages_router.get("/users/me")
async def get_current_user():
  return {"message": "This is the current user"}

@general_pages_router.get("/users/{user_id}")
async def get_user_id(user_id: int):
  return {"user_id": user_id}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@general_pages_router.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}

    if food_name.value == "fruits":
        return {
            "food_name": food_name,
            "message": "you are still healthy, but like sweet things",
        }
    return {"food_name": food_name, "message": "i like chocolate milk"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@general_pages_router.get('/tasks')
def find_all_tasks(request: Request):
    tasks = ['task 1', 'task 2', 'task 3']
    return templates.TemplateResponse("tasks.html", {"request": request, 'tasks': tasks})