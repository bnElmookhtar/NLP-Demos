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
```
tailorcv/
├── backend
│ ├── services/
│ │ ├── analyzer.py       # Core logic to compare CV and JD
│ │ ├── pdf_parser.py     # Extracts text from PDF CVs
│ │ ├── preprocessing.py  # Cleans & prepares job description for analysis
| | └── main.py           # API for dealing with frontend 
│ └── Dockerfile          # Docker file for backend
|
|
├── frontend
│ ├── index.html            # Home page for this site
│ └── assets/
│      ├── images
|      |    ├── logo.png    # App logo
│      ├── css
|      |    └── styles.css  # The style of the home page
|      └── Js
|          └── scripts.js   # Home page interactions
│ 
├── README.md
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js (for frontend development, optional)
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/bnElmookhtar/NLP-Demos/tree/main/TailorCV.git
   cd tailorcv
   ```

2. **Backend setup:**
   ```sh
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Copy `.env` and add your Google API key for Gemini:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```

4. **Frontend setup (optional):**
   - The frontend is static and can be opened directly in a browser.
   - For development, you can use a simple HTTP server:
     ```sh
     cd frontend
     python -m http.server 8080
     ```

---

## Usage

1. **Start the backend API:**
   ```sh
   cd backend
   uvicorn services.main:app --reload
   ```
   The API will be available at `http://127.0.0.1:5000`.

2. **Open the frontend:**
   - Open `frontend/index.html` in your browser, or visit `http://localhost:8080` if using a local server.

3. **Analyze your CV:**
   - Paste a Job Description and upload your CV (PDF).
   - Click "Analyze" to receive tailored recommendations.

---

## API

The backend exposes a single endpoint:

- `POST /analyze`
  - **Form fields:**
    - `job_description` (str, required)
    - `cv` (file, optional)
    - `cv_text` (str, optional)
  - **Response:**
    ```json
    {
      "matchScore": 85,
      "objective": "...",
      "skills": ["Python", "NLP", ...],
      "keywords": ["LLM", "LangChain", ...],
      "recommendations": [
        "Update your objective to: ...",
        "Highlight these skills: ...",
        "Consider adding keywords: ..."
      ]
    }
    ```

---

## Extending

- Add new analysis logic in [`backend/services/analyer.py`](backend/services/analyer.py).
- To support more file types, extend [`backend/services/pdf_parser.py`](backend/services/pdf_parser.py).
- For additional preprocessing, modify [`backend/services/preprocessing.py`](backend/services/preprocessing.py).

---

## License

MIT License

---

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [Google Gemini](https://ai.google.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)