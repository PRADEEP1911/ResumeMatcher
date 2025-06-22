# ResumeMatcher-FA

A smart AI-powered web application that matches **resumes with job descriptions** using NLP techniques like **TF-IDF** and **vector similarity**.  
Built with **FastAPI**, it extracts, processes, and scores resume content to help recruiters and job-seekers analyze compatibility instantly.

---

## 🚀 Features
✅ Upload Resume & Job Description (PDF/Text)  
✅ Automatic Resume Parsing and Keyword Extraction  
✅ TF-IDF based Vectorization & Matching Algorithm  
✅ Similarity Score to Measure Resume-Job Fit  
✅ Clean Web Interface (Jinja2 + HTML/CSS)  
✅ Supports multiple resume files (extendable)

---

## Folder Structure
- main.py # FastAPI backend
- requirements.txt # Project dependencies
- Uploads/ # Folder to store uploaded resumes
- templates/
    - index.html # Frontend HTML (Jinja2)
- README.md

---

## 🛠️ Tech Stack
- **Python 3.x**
- **FastAPI** – lightweight API backend
- **Jinja2** – templating engine for dynamic HTML
- **NLP** – using `TF-IDF`, cosine similarity
- **scikit-learn** – for vectorization
- **Uvicorn** – ASGI server for FastAPI
- **HTML/CSS** – basic UI layout



---

## ⚙️ Tech Stack

- **Python 3.x**
- **FastAPI** – lightweight API backend
- **Jinja2** – templating engine for dynamic HTML
- **NLP** – using `TF-IDF`, cosine similarity
- **scikit-learn** – for vectorization
- **Uvicorn** – ASGI server for FastAPI
- **HTML/CSS** – basic UI layout

---

## 📦 Installation & Run Locally

> Clone the repo and run locally in a few simple steps 👇

```bash
# Step 1: Clone the repository
git clone https://github.com/yourusername/ResumeMatcher-FA.git

# Step 2: Move into the project folder
cd ResumeMatcher-FA

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the server
uvicorn main:app --reload

---
