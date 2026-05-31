import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    "nemotron-3-super-fp4",
    model_provider="openai",
    base_url=os.environ.get("KIMCHI_BASE_URL"),
    api_key=os.environ.get("KIMCHI_KEY"),
)

result = model.invoke("What is the capital of India?")

print(result.content)
