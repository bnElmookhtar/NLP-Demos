from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import json
from pdf_parser import extract_cv_content
from preprocessing import extract_keywords_rake, clean_job_description


# Load API key from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")


# Init LLM (flash is lighter than pro)
llm = ChatGoogleGenerativeAI(
    temperature=0,
    model="gemini-1.5-flash",
    api_key=GOOGLE_API_KEY
)


# Prompt template
template = """
You are an expert career assistant.
Based on the following job description:

{job_description}

Please rewrite the following CV to better fit this job.
Return the CV in JSON format with the following keys:
- objective
- education
- courses
- experience
- skills

Here is the CV:
{cv_text}
"""

prompt = PromptTemplate(
    input_variables=["job_description", "cv_text"],
    template=template
)

chain = prompt | llm


def rewrite_cv_for_job(cv_path: str, job_description: str) -> dict:
    """
    Rewrite CV to match a job description and return JSON object.
    
    Args:
        cv_path (str): Path to CV PDF file
        job_description (str): Job description text
    
    Returns:
        dict: Rewritten CV structured in JSON format
    """
    # Clean job description
    job_description_clean = clean_job_description(job_description)

    # Extract CV text
    cv_text = extract_cv_content(cv_path)

    # Run chain
    response = chain.invoke({
        "job_description": job_description_clean,
        "cv_text": cv_text
    })

    # Parse JSON safely
    try:
        rewritten_cv = json.loads(response.content)
    except json.JSONDecodeError:
        # fallback: wrap in dict if model returned plain text
        rewritten_cv = {"raw_response": response.content}

    return rewritten_cv


# Example usage
if __name__ == "__main__":
    cv_json = rewrite_cv_for_job(
        "D:\\Data\\DataSciense\\NLP\\projects\\NLP-Demos\\TailorCV\\backend\\services\\cv.pdf",
        "We are hiring a Data Scientist with Python, NLP, SQL, and Machine Learning."
    )
    print(json.dumps(cv_json, indent=2, ensure_ascii=False))
