from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
import re

from services.analyer import rewrite_cv_for_job   
from  services.pdf_parser import extract_cv_content

app = FastAPI()

# to allow connection with frontend 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze")
async def analyze(
    job_description: str = Form(...),
    cv_text: str = Form(None),               
    cv: UploadFile | None = None           
):
    

    # extract cv content
    final_cv_text = ""
    if cv:  
        final_cv_text = extract_cv_content(cv.file)
    elif cv_text: 
        final_cv_text = cv_text

    if not final_cv_text:
        return {"error": "CV content is empty. Please upload a PDF or provide text."}

    rewritten_cv = rewrite_cv_for_job(
        job_description=job_description,
        cv_text=final_cv_text
    )

    raw = rewritten_cv.get("raw_response", "")

    cleaned = re.sub(r"```json|```", "", raw).strip()

    parsed = json.loads(cleaned)

    return {
    "matchScore": parsed.get("matchScore", 0),
    "objective": parsed.get("objective", ""),
    "skills": parsed.get("skills", []),
    "keywords": parsed.get("recommendedKeywords", []),
    "recommendations": [
        f"Update your objective to: {parsed.get('objective','')}",
        f"Highlight these skills: {', '.join(parsed.get('skills', []))}",
        f"Consider adding keywords: {', '.join(parsed.get('recommendedKeywords', []))}"
    ]
}


   

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
