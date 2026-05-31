import os

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model=os.environ.get("GOOGLE_MODEL"),
)

result = model.invoke("What is the capital of Thailand?")

print(result.content)
