# VoxaBrief
## VoxaBrief is a web-based platform that allows users to upload any audio recording and automatically:

1. Convert it into a format suitable for processing.  
2. Transcribe the audio to **Arabic text** using an AI speech recognition model.  
3. Generate a **concise summary** of the transcription using AI.  
4. Optionally send the summary to **Telegram** for notifications.

This project demonstrates an end-to-end **speech-to-text and summarization pipeline** leveraging modern AI tools.

---
## Features

- **Multi-format support:** Accepts MP3, WAV, OPUS, and other audio formats.  
- **Automatic preprocessing:** Converts audio to mono, 16kHz WAV for optimal model performance.  


```
VoxaBrief/
│
├── app/
│ ├── main.py # FastAPI app entrypoint
│ ├── services/
│ │ ├── audio_processing.py # Audio conversion, resampling, chunking
│ │ ├── transcription.py # Arabic speech-to-text
│ │ ├── summarizer.py # Text summarization
│ │ └── telegram.py # Send summary to Telegram
│ ├── utils/
│ │ └── chunking.py # Split long audio into manageable chunks
│ └── config.py # API keys & constants
│
├── templates/ # Web UI
│ └── index.html
├── static/ #  CSS/JS
├── requirements.txt # Python dependencies
├── Dockerfile # Optional containerization
├── .env # Environment variables (keys, tokens)
└── README.md # Project documentation
```