# reviewer.py

import os
from datetime import datetime

def load_spun_version(chapter_id: int, version: int = 1):
    file_path = f"outputs/chapter_{chapter_id}_spun_v{version}.txt"
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Spun file not found: {file_path}")
    
    with open(file_path, "r") as f:
        return f.read()

def save_edited_version(chapter_id: int, content: str, new_version: int):
    out_path = f"outputs/chapter_{chapter_id}_spun_v{new_version}.txt"
    with open(out_path, "w") as f:
        f.write(content)
    
    print(f"✅ Saved edited version to {out_path}")

def main():
    chapter_id = 1
    base_version = 1
    new_version = 2

    print("📖 Loading spun content...")
    original_text = load_spun_version(chapter_id, base_version)
    print("\n📝 Original Spun Text:\n")
    print(original_text)

    print("\n✍️ Enter your revised version (end with a single line containing just 'EOF'):\n")
    lines = []
    while True:
        line = input()
        if line.strip() == "EOF":
            break
        lines.append(line)
    
    edited_text = "\n".join(lines)

    save_edited_version(chapter_id, edited_text, new_version)

if __name__ == "__main__":
    main()
