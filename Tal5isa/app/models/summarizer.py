from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('google/flan-t5-small')
model = T5ForConditionalGeneration.from_pretrained('google/flan-t5-small')

def summarize(text: str) -> str:
  
    tokens = tokenizer("summarize: " + text, return_tensors='pt', truncation=True, padding='longest')

    summary_ids = model.generate(
        **tokens,
        max_length=80,
        min_length=40,
        num_beams=4,
        length_penalty=2.0,
        early_stopping=True
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
