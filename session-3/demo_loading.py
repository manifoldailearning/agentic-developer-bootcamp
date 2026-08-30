from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))
print(os.getenv("OPENAI_MODEL"))