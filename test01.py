from playwright.sync_api import Page
import pytest

def test_title(page: Page):
    page.goto("https://developer.mozilla.org/en-US/")
    assert page.title() == "MDN Web Docs"
