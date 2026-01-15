# 🧠 NLP Demos – Explore Real-World NLP Applications

**NLP Demos** is a collection of **end-to-end, production-ready web applications** that let you experience and play with powerful NLP tasks in a practical way.

---

## ✨ Current Live Demos

| Project       | Description                                      | Tech Stack                  | Status      | Last Updated     |
|---------------|--------------------------------------------------|-----------------------------|-------------|------------------|
| **AskGenie**  | Intelligent SQL question answering from databases | Streamlit + Gemini          | Active      | 1 minute ago     |
| **ChatYourDB**| Natural language to SQL + execution              | Streamlit + LLM             | Active      | 1 minute ago     |
| **Tal5ia**    | Smart text summarization (Extractive & Abstractive) | FastAPI / Streamlit       | Active      | 5 months ago     |
| **TailorCV**  | AI-powered smart CV/resume customizer            | FastAPI + LLM               | Active      | 5 months ago     |
| **SmartFuncBooker** | Smart function booking & scheduling assistant | -                        | In progress | 4 months ago     |
| **VibeVoice** | Advanced text-to-speech & voice generation       | -                           | Setup only  | 5 months ago     |
| **VoxaBrief** | Short-form audio content generation (?)          | -                           | Setup only  | -                |

---

## 🚀 Key Features Across Projects

- Natural Language to SQL generation & execution
- High-quality text summarization (extractive + abstractive)
- AI-assisted CV/resume tailoring & optimization
- Text-to-Speech (coming soon)
- Modern web interfaces (mostly Streamlit + some FastAPI backends)

---

## 🛠️ How to Run Any Demo Locally

Most projects follow this simple structure:

```bash
# 1. Go to the project folder
cd AskGenie          # or Tal5ia, TailorCV, etc.

# 2. Create & activate virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
# or
.venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Set up environment variables
cp .env.example .env
# → edit .env with your API keys (Gemini, OpenAI, etc.)

# 5. Run the app
streamlit run app.py         # most common
# or
python main.py               # for FastAPI projects
