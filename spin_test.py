from scraper_module import scrape_chapter
from local_llm_module import spin_chapter_locally
import os

# Step 1: Scrape
url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
raw_text = scrape_chapter(url)

# Step 2: Spin
spun = spin_chapter_locally(raw_text)

# Step 3: Save
os.makedirs("outputs", exist_ok=True)
with open("outputs/chapter_1_spun_v1.txt", "w") as f:
    f.write(spun)

print("✅ Chapter scraped, spun, and saved to outputs/chapter_1_spun_v1.txt")
