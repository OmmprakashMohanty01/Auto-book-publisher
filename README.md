# 📘 Auto Book Publisher

This project demonstrates an automated workflow for scraping book chapters, rewriting them using a local LLM (Ollama + Mistral), reviewing the content with human input, storing chapter versions in ChromaDB, and retrieving them with semantic search.

---

## 🚀 Features

* 🔸 Web scraping using **Playwright**
* 🧠 AI rewriting via **Ollama + Mistral (local LLM)**
* ✍️ Human-in-the-loop **manual editing**
* 📂 Versioned storage using **ChromaDB**
* 🔍 Intelligent search via **sentence-transformer embeddings**

---

## 📁 Project Structure
.
├── chapter_raw.txt               # Raw chapter after scraping
├── chapter_screenshot.png       # Screenshot of scraped page
├── chroma_db/                   # Persistent ChromaDB store
├── outputs/                     # Folder for spun and reviewed chapters
├── screenshots/                 # Saved browser screenshots
├── scraper.py                   # Web scraping logic
├── spin_test.py                 # Calls local LLM to spin content
├── reviewer.py                  # Accepts or edits spun content
├── store_reviewed_chapter.py   # Saves reviewed content to ChromaDB
├── search_chapter.py           # Searches for chapters based on a query
├── vector_store.py             # ChromaDB-related logic
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

---

## 🛠️ How to Run the Workflow

### 1. Clone the Repository

git clone https://github.com/OmmprakashMohanty01/Auto-book-publisher.git
cd auto-book-publisher

### 2. Set Up Your Environment

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install

### 3. Scrape a Chapter

python scraper.py

* ✅ Saves chapter as: `chapter_raw.txt`
* 📸 Screenshot saved as: `chapter_screenshot.png`

### 4. Spin the Chapter Using Local LLM

Ensure Ollama is running and the `mistral` model is pulled:

ollama run mistral

## Then run:

python spin_test.py

* ✅ Output saved to: `outputs/spun_chapter.txt`

---

### 5. Review & Edit the Spun Text (Human-in-the-loop)

python reviewer.py

* View spun content in the terminal.
* Make edits or type `EOF` if no changes are needed.
* ✅ Final version saved to: `outputs/chapter_1_spun_v2.txt`

---

### 6. Save Reviewed Chapter to ChromaDB

#### 📦 First-time Only: Install Extra Dependency

pip install sentence-transformers

#### Save Chapter to Vector Store

python store_reviewed_chapter.py

* ✅ Stores chapter version `chapter_1_v2` to ChromaDB with embeddings

---

### 7.🔍 Search for a Chapter (RL-based Retrieval)

Once you've stored one or more reviewed chapters, you can perform a search across them:

python search_chapter.py

This will prompt you to enter a query. For example:

🔎 Enter your search query: who is Tari?

The script will use embedding-based similarity search (RL-like logic) to return the most relevant saved chapter content.

---
## 🔍 Optional: View Stored Documents

python debug_list_docs.py

## 📌 Notes

* All outputs are stored inside the `outputs/` directory.
* Embedding model used: `all-MiniLM-L6-v2`
* Vector DB is saved under `chroma_db/`

---

## 🔮 Coming Soon

* RL-based semantic search engine over stored content
* Full web interface for human review and search

---

## 🧪 Tested On

* ✅ Python 3.12
* ✅ macOS + Ollama (Mistral model)
* ✅ ChromaDB v0.4+

---
## 🧠 Credits

Built by Omm Prakash Mohanty using:

* Python 🐍
* Playwright for scraping 🌐
* Ollama + Mistral for local LLMs 🤖
* ChromaDB for versioned vector storage 📚
* Sentence Transformers for semantic search 🔍

## 👨‍💼 Author

[Omm Prakash Mohanty](https://github.com/OmmprakashMohanty01)


📄 License
⚠️ This project is for evaluation purposes only and is not intended for commercial use