# search_chapter.py
from vector_store import search_chapters

if __name__ == "__main__":
    query = input("\n🔍 Enter your search query: ")

    results = search_chapters(query, top_k=3)

    if not results:
        print("❌ No results found.")
    else:
        print("\n📚 Top Matching Results:\n")
        for i, r in enumerate(results, 1):
            print(f"🔹 Result {i}")
            print(f"📄 Doc ID     : {r['id']}")
            print(f"📊 Score      : {round(r['score'], 4)}")
            print(f"📝 Text Chunk :\n{r['text']}\n")
            print("-" * 50)
