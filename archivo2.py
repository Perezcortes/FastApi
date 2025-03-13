import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://developer.mozilla.org/en-US/")
        print(await page.title())
        assert await page.title() == "MDN Web Docs"
        print("Test complete")
        browser.close()
    print("test async")

asyncio.run(main())
