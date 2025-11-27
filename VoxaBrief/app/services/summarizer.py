import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure GenAI API key once globally
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
if not GENAI_API_KEY:
    raise RuntimeError("GENAI_API_KEY is not set in environment variables!")

genai.configure(api_key=GENAI_API_KEY)


def summarize_text(text: str, selected_model: str = None) -> str:
    """
    Summarizes the given text using the Gemini API.

    Args:
        text (str): The transcription text in Arabic.
        selected_model (str, optional): The Gemini model to use. Defaults to environment variable or gemini-2.5-flash.

    Returns:
        str: The summarized text in bullet points.
    """
    if not text.strip():
        return " لا يوجد نص لمعالجته."

    # Use model from parameter, env, or default
    model_name = selected_model or os.getenv("GENAI_MODEL") or "gemini-2.5-flash"

    prompt = f"""
أريد منك تلخيص النص التالي (وهو تفريغ صوتي باللهجة العربية) في شكل نقاط موجزة وواضحة، جاهزة للإرسال على تليغرام.

المطلوب تحديداً:
- كتابة ملخص قصير جداً بدون تفاصيل غير ضرورية.
- عرض الملخص في نقاط واضحة (Bullet Points).
- استخدام لغة عربية فصحى بسيطة ومفهومة.
- التركيز فقط على أهم الأفكار والرسائل الأساسية.
- عدم إعادة صياغة النص بالكامل، فقط استخراج أهم النقاط.
- عدم إضافة معلومات غير موجودة في النص.

النص المراد تلخيصه:
====================
{text}
====================

الرجاء إخراج النتيجة بالشكل التالي فقط:

📌 **النقاط الأساسية:**
- …
- …
- …
"""

    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        # Sometimes response.text may be None, fallback to first candidate
        summary = getattr(response, "text", None)
        if not summary and getattr(response, "candidates", None):
            summary = response.candidates[0].text
        return summary or " لم يتم توليد الملخص."
    except Exception as e:
        return f" حدث خطأ أثناء التلخيص: {e}"


if __name__ == "__main__":
    sample_text = "هنا يمكن وضع نص تجريبي للتلخيص."
    summary = summarize_text(sample_text)
    print(summary)
