# TailorCV  

**TailorCV** is a tool that automatically improves your resume (CV) based on a specific Job Description (JD).  
Users upload a CV (PDF) and provide a Job Description. The system analyzes both and suggests improvements, missing skills, and generates a tailored version of the CV.  

---

## Features  
- Upload a **CV (PDF)** and a **Job Description (JD)**.  
- Automatic analysis of CV content vs. JD requirements.  
- Suggestions for improvements and missing skills.  
- Generates LaTeX code for a tailored CV.  
- Modular backend structure for easy extension.  

---

## Project Structure 

tailorcv/
├── backend
│ ├── routes/
│ │ └── cv_routes.py # API routes for CV analysis
│ │
│ ├── services/
│ │ ├── analyzer.py # Core logic to compare CV and JD
│ │ ├── pdf_parser.py # Extracts text from PDF CVs
│ │ └── preprocessing.py # Cleans & prepares job description for analysis
│ │
│ ├── README.md
│ └── requirements.txt

