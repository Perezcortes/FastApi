from playwright.sync_api import Page, sync_playwright
import pytest

def test_title(page: Page):
    page.goto("https://github.com/login")
    assert page.title() == "Sign in to GitHub · GitHub"

def test_title2(page: Page):
    page.goto("https://github.com")
    assert page.title() == "GitHub · Build and ship sof"
