from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import time

tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

def summarize(text: str) -> str:
    start = time.time()

    inputs = tokenizer("summarize: " + text, return_tensors='pt', truncation=True, padding='longest').to(device)

    summary_ids = model.generate(
        **inputs,
        max_length=80,
        min_length=30,
        num_beams=1,
        length_penalty=1.0,
        early_stopping=True
    )

    result = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    print("Summarization took:", round(time.time() - start, 2), "sec")
    return result
