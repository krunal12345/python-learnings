import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://llm.kimchi.dev/openai/v1",
    api_key=os.environ.get("KIMCHI_KEY"),
)

completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what is the capital of India?",
        }
    ],
    model="kimi-k2.5",
)

print(completion.choices[0].message)
