# main.py
import os
import json
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from preprocessing import extract_keywords_rake, clean_job_description

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    temperature=0,
    model="gemini-1.5-flash",
    api_key=GOOGLE_API_KEY
)

template = """
You are an expert career assistant.
Based on the following job description:

{job_description}

Please rewrite the following CV to better fit this job.
Return the result strictly in JSON format with the following keys:
- objective
- education
- courses
- experience
- skills
- matchScore (0-100, how well the CV matches the job)
- recommendedKeywords (list of important keywords missing from the CV)

Here is the CV:
{cv_text}
"""

prompt = PromptTemplate(
    input_variables=["job_description", "cv_text"],
    template=template
)

chain = prompt | llm


def rewrite_cv_for_job(job_description: str, cv_text: str) -> dict:
    job_description_clean = clean_job_description(job_description)

    response = chain.invoke({
        "job_description": job_description_clean,
        "cv_text": cv_text
    })

    try:
        rewritten_cv = json.loads(response.content)
    except json.JSONDecodeError:
        rewritten_cv = {"raw_response": response.content}

    if "matchScore" not in rewritten_cv:
        rewritten_cv["matchScore"] = 0
    if "recommendedKeywords" not in rewritten_cv:
        rewritten_cv["recommendedKeywords"] = extract_keywords_rake(job_description_clean)
    
    

    return rewritten_cv
