# 🧠 Tal5isa - Text Summarization Web App

**Tal5isa** (تلخيصه) is an end-to-end web application that allows users to input long text and receive a concise summary using machine learning. Built with Flask for the backend and trained NLP models, the app provides an intuitive interface and customizable architecture.

---

## 🚀 Features

- Extractive and abstractive summarization of input text
- Clean and responsive web interface
- Modular Flask application structure
- Easy model integration and retraining
- Includes Jupyter notebooks for experimentation
- Testing suite for model evaluation

---

## 🗂️ Project Structure
Tal5isa/ │ ├── README.md # Project documentation ├── app/ │ ├── __init__.py # Flask app factory │ ├── routes.py # API and web routes │ ├── models/ # Model loading and inference code │ ├── templates/ │ │ └── index.html # Main web UI (React + Tailwind) │ └── utils/ # Utility functions │ ├── notebooks/ │ ├── abstracive.ipynb # Abstractive summarization experiments │ └── extractive.ipynb # Extractive summarization experiments │ ├── static/ │ └── assets/ │ ├── css/ # Custom styles │ ├── images/ │ │ └── logo.png # App logo │ └── js/ # Custom scripts │ ├── tests/ # Unit and integration tests └── trained_models/ └── tfidf_vectorizer.pkl # Pretrained vectorizer for extractive summarization


---

## ⚡ Quick Start

1. **Clone the repository:**
   ```sh
   git clone https://github.com/bnElmookhtar/Tal5isa.git
   cd Tal5isa


Notebooks
    notebooks/abstracive.ipynb: Abstractive summarization with T5 and Pegasus.
    notebooks/extractive.ipynb: Extractive summarization using TF-IDF and TextRank.