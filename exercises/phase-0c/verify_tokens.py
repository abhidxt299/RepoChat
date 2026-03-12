from dotenv import load_dotenv
import os

load_dotenv()

groq_key = os.getenv("GROQ_TOKEN")
github_token = os.getenv("GITHUB_TOKEN")

print("Groq key loaded:", bool(groq_key))
print("GitHub token loaded:", bool(github_token))