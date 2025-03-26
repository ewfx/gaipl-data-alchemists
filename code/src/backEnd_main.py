from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define request model
class ChatRequest(BaseModel):
user_query: str

@app.post("/chat/")
async def chat_with_ai(request: ChatRequest):
try:
response = openai.ChatCompletion.create(
model="gpt-4",
messages=[{"role": "user", "content": request.user_query}]
)
return {"response": response["choices"][0]["message"]["content"]}
except Exception as e:
raise HTTPException(status_code=500, detail=str(e))


Front end code: chatbot.js