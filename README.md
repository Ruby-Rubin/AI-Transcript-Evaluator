# 🎓 AI Transcript Evaluator

AI Transcript Evaluator is a hybrid AI-powered system that evaluates spoken responses from video recordings. The application uses Whisper for transcription, local NLP techniques for objective metrics, and Gemini for subjective evaluation.

## 🚀 Features

- Video Upload
- Whisper Transcription
- Grammar Evaluation
- Vocabulary Evaluation
- Clarity Assessment
- Technical Accuracy Evaluation
- Professionalism Analysis
- Interactive Dashboard

## 🏗️ Architecture

```mermaid
flowchart TD
    A[Video Upload] --> B[Whisper Transcription]
    B --> C[Transcript]

    C --> D[Grammar Local]
    C --> E[Vocabulary Local]
    C --> F[Clarity Gemini]
    C --> G[Technical Accuracy Gemini]
    C --> H[Professionalism Gemini]

    D --> I[Final Evaluation Report]
    E --> I
    F --> I
    G --> I
    H --> I

    I --> J[Streamlit Dashboard]
```

## ⚙️ Tech Stack

- Streamlit
- Whisper
- Gemini
- LanguageTool
- LexicalRichness
- Matplotlib

## 🛠️ Installation

```bash
git clone https://github.com/Ruby-Rubin/AI-Transcript-Evaluator.git
cd AI-Transcript-Evaluator
pip install -r requirements.txt
streamlit run streamlit_app.py
