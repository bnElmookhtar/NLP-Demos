from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

generator = pipeline("text2text-generation", model="google/flan-t5-small")

class PromptRequest(BaseModel):
    prompt: str
    prompt_type: str
    temperature: float = 0.7


@app.post("/ask")
async def ask_ai(data: PromptRequest):
    prompt = data.prompt
    prompt_type = data.prompt_type
    temperature = data.temperature

    if prompt_type == "zero-shot":
        final_prompt = prompt
    elif prompt_type == "few-shot":
        final_prompt = f"مثال: سؤال: ما هي عاصمة فرنسا؟ إجابة: باريس.\nالآن سؤال: {prompt}"
    elif prompt_type == "chain-of-thought":
        final_prompt = f"حل السؤال خطوة بخطوة:\n{prompt}"
    elif prompt_type == "generated-knowledge":
        final_prompt = f"معلومة: شركة آبل تأسست عام 1976.\nالآن جاوب: {prompt}"
    elif prompt_type == "self-refine":
        final_prompt = f"جاوب على السؤال ثم راجع إجابتك وعدلها لو لقيت خطأ:\n{prompt}"
    else:
        final_prompt = prompt

    response = generator(
        final_prompt,
        max_length=200,
        temperature=temperature,
    )

    return {"answer": response[0]["generated_text"]}
