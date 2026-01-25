import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill(
        "Get some Norsh puss")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill(
        "Lick a titty")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.screenshot(path="norsh_demo.png")
