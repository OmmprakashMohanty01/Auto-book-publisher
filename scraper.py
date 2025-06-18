# scraper.py
from playwright.sync_api import sync_playwright

def fetch_chapter(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        # Save screenshot
        page.screenshot(path="chapter_screenshot.png")

        # Extract all text from the body
        content = page.inner_text("body")

        browser.close()
        return content

# Test the function
if __name__ == "__main__":
    test_url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    chapter_text = fetch_chapter(test_url)
    
    with open("chapter_raw.txt", "w") as f:
        f.write(chapter_text)

    print("✅ Chapter fetched and saved to 'chapter_raw.txt'")
    print("🖼 Screenshot saved as 'chapter_screenshot.png'")
