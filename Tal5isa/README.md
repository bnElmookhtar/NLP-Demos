# 🧠 Tal5isa - Text Summarization Web App

**Tal5isa** (تلخيصه) is an end-to-end web application that allows users to input long text and receive a concise summary using machine learning. Built with Flask for the backend and trained NLP models, the app provides an intuitive interface and customizable architecture.

---

![Logo](static/assets/images/logo.png)


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
