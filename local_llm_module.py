import subprocess

def spin_chapter_locally(text):
    prompt = f"""You are a vivid writer. Rewrite the following chapter to make it modern, engaging, and easy to read without changing the meaning:

{text}
"""
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=300  # 5 minutes max
        )
        return result.stdout.decode().strip()
    except subprocess.TimeoutExpired:
        return "⚠️ Local model took too long to respond."
