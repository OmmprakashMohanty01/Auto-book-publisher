# vector_store.py
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# Use new client interface (no Settings object)
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="book_chapters",
    embedding_function=SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
)

def save_chapter_version(doc_id, text):
    chunks = text.split("\n\n")  # Paragraph-based chunking
    documents = [chunk.strip() for chunk in chunks if chunk.strip()]
    ids = [f"{doc_id}_chunk{i}" for i in range(len(documents))]
    metadatas = [{"chapter_id": doc_id, "chunk_index": i} for i in range(len(documents))]
    
    collection.add(documents=documents, ids=ids, metadatas=metadatas)
    print(f"✅ Saved: {doc_id}")

def search_chapters(query, top_k=5):
    results = collection.query(query_texts=[query], n_results=top_k)
    
    if not results or not results['documents'][0]:
        return []

    output = []
    for doc_id, doc, score in zip(results["ids"][0], results["documents"][0], results["distances"][0]):
        output.append({
            "id": doc_id,
            "text": doc,
            "score": score
        })
    return output
