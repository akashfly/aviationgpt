# ✈ AviationGPT — AI Copilot for Aviators

AviationGPT is an AI-powered aviation assistant built for DGCA ground school students, trainee pilots, and aviation professionals.

It allows users to ask aviation-related questions in natural language and receive context-aware answers from uploaded training material.

---

# Features

## 1. Aviation Q&A
Ask questions related to:

- Air Navigation
- Meteorology
- Technical General
- Regulations
- DGCA Ground Classes
- Aircraft Systems
- Procedures

Questions are answered using semantic search from uploaded study material.

---

## 2. Voice to Text
Users can record voice directly from the browser.

Speech is converted into text using Google Speech Recognition.

Useful for:
- hands-free querying
- cockpit-style interaction
- quick verbal questioning

---

## 3. PDF Upload
Upload aviation PDFs such as:

- DGCA notes
- SOP manuals
- Ground school notes
- checklists

---

## 4. Image Upload
Upload:

- aircraft system diagrams
- instrument panels
- charts
- screenshots

for future multimodal aviation assistance.

---

## 5. Semantic Search with FAISS
The application uses:

- LangChain
- FAISS Vector Database
- HuggingFace Sentence Transformers

to retrieve relevant chunks from aviation study content.

---

# Tech Stack

## Frontend
- Gradio

## Backend
- Python

## AI / NLP
- LangChain
- FAISS
- HuggingFace Embeddings

## Speech Recognition
- SpeechRecognition Library

## Deployment
- Hugging Face Spaces

---

# Project Structure

```bash
AviationGPT/
│
├── app.py
├── requirements.txt
├── README.md
├── vectorstore/
│
└── data/
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/AviationGPT.git
```

Move inside:

```bash
cd AviationGPT
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

---

# Future Improvements

- OCR from uploaded aviation documents
- Image understanding for cockpit instruments
- LLM-generated answers
- Chat memory
- Pilot checklist assistant
- DGCA exam preparation mode
- ATPL question bank integration

---

# Author

Built by Sai.

AI Copilot for Aviators ✈
