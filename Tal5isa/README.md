# 🧠 Tal5isa - Text Summarization Web App

**Tal5isa** (تلخيصه) is an end-to-end web application that allows users to input long text and receive a concise summary using machine learning. Built with Flask for the backend and trained NLP models, the app provides an intuitive interface and customizable architecture.

---

![Logo](static/assets/images/logo.png)

## APP screen
![screen](https://github.com/bnElmookhtar/NLP-Demos/blob/main/Tal5isa/app/static/assets/images/app-page.png?raw=true)


## 🚀 Features

- Extractive and abstractive summarization of input text
- Clean and responsive web interface
- Modular Flask application structure
- Easy model integration and retraining
- Includes Jupyter notebooks for experimentation
- Testing suite for model evaluation

---

```
## 🗂️ Project Structure
Tal5isa/
├── app/                           # Flask backend
│   ├── __init__.py                # Flask app factory
│   ├── routes.py                  # API and web routes
│   ├── models/                    # Model loading and inference
│   ├── utils/                     # Helper functions
│   ├── templates/                 # HTML templates
│   │   └── index.html             # Main UI (HTML + Tailwind)
│
├── static/                        # Frontend static assets
│   └── assets/
│       ├── css/                   # Custom styles
│       ├── js/                    # Custom scripts
│       └── images/
│           └── logo.png           # App logo
│
├── notebooks/                     # Jupyter experiments
│   ├── abstracive.ipynb           # Abstractive summarization
│   └── extractive.ipynb           # Extractive summarization
│
├── trained_models/                # Pretrained models and vectorizers
│   └── tfidf_vectorizer.pkl       # TF-IDF vectorizer
│
├── tests/                         # Unit and integration tests
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
````

---

## ⚡ Quick Start

1. **Clone the repository:**
   ```sh
   git clone https://github.com/bnElmookhtar/Tal5isa.git
   cd Tal5isa


2. **Set up a virtual environment:**
      ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt

4. **Run the FastAPI server:**
   ```sh
   uvicorn app.main:app --reload

5. **Open the app:**
   ```sh
   http://127.0.0.1:8000
   


##  Technologies Used

- **FastAPI**  
  A high-performance web framework for building modern APIs with Python 3.7+.

- **Transformers (Hugging Face)**  
  For loading and running state-of-the-art NLP models like T5 for abstractive summarization.

- **Tailwind CSS**  
  A utility-first CSS framework used for responsive and clean UI styling.

- **Jinja2**  
  Lightweight templating engine used to render HTML pages with dynamic data.

- **Uvicorn**  
  ASGI web server used to serve the FastAPI app in production and development.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-00cc99?logo=fastapi)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-Utility--First-38bdf8?logo=tailwindcss)
![HTML5](https://img.shields.io/badge/HTML-5-orange?logo=html5)
![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-yellow?logo=huggingface)


