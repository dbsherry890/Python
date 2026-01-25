import pyautogui as ag
import time
import subprocess
import platform
import webbrowser

ag.FAILSAFE = True
ag.PAUSE = 0.5


def open_chrome():
    system = platform.system()

    if system == "Darwin":  # macOS
        subprocess.Popen(["open", "-a", "Google Chrome"])
    elif system == "Windows":
        subprocess.Popen(["start", "chrome"], shell=True)
    elif system == "Linux":
        subprocess.Popen(["google-chrome"])
    else:
        raise Exception("Unsupported OS")

    time.sleep(2)  # Give Chrome time to open


def goto_youtube():
    # Easiest / most reliable way:
    webbrowser.open("https://www.youtube.com")
    time.sleep(3)


def search_youtube(query):
    ag.hotkey("/")

    ag.typewrite(query, interval=0.02)
    ag.press("enter")


open_chrome()
goto_youtube()
search_youtube("bmx videos recent")
