from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

# Initialize FastAPI app
app = FastAPI()

# Set your OpenAI API Key (Replace with your actual API Key)
openai.api_key = "YOUR_OPENAI_API_KEY"

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