# store_reviewed_chapter.py

from vector_store import save_chapter_version

# Load the reviewed chapter text
with open("outputs/chapter_1_spun_v2.txt", "r") as f:
    reviewed_text = f.read()

# Save to vector database
save_chapter_version(doc_id="chapter_1_v2", text=reviewed_text)
