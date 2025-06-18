# 📘 Automated Book Publication Workflow

This project automates the workflow of collecting chapters from web sources, rewriting them using AI, reviewing them via human-in-the-loop steps, and storing everything with versioning and semantic search.

---

## 🚀 Features

- 🕸️ Web scraping using Playwright
- ✍️ AI Writer using Ollama + Mistral (local LLM)
- 🧠 Human-in-the-loop review and editing
- 💾 Versioning via ChromaDB
- 🔎 Intelligent search using embeddings

---

## 📁 Folder Structure

auto-book-publisher/
├── outputs/ # Contains spun & reviewed chapters
├── screenshots/ # Screenshot images from scraping
├── chroma_db/ # ChromaDB persistent vector store
├── scrape_chapter.py # Web scraping logic
├── ai_writer.py # AI rewriting module (Ollama)
├── ai_reviewer.py # Optional reviewer logic
├── store_reviewed_chapter.py # Saves reviewed content to ChromaDB
├── search_chapter.py # Retrieves text using semantic search
├── vector_store.py # Handles all ChromaDB operations
├── debug_list_docs.py # Utility to debug stored docs
├── requirements.txt # List of dependencies
└── README.md # You're reading it.


---

## 🛠️ How to Run

### 1. Clone the Repo

git clone https://github.com/your-username/auto-book-publisher.git
cd auto-book-publisher
 
 ### 2. Install Dependencies

 pip install -r requirements.txt
 playwright install

### 3. Run the Workflow

# Scrape chapter
python scrape_chapter.py

# Spin using local LLM
python ai_writer.py

# (Optional) AI review
python ai_reviewer.py

# Save to ChromaDB
python store_reviewed_chapter.py

# Search
python search_chapter.py

📄 License
⚠️ This project is for evaluation purposes only and is not intended for commercial use