from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import docx2txt
import PyPDF2
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()
templates = Jinja2Templates(directory="templates")
UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        text = ""
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text
    elif file_path.endswith(".docx"):
        return docx2txt.process(file_path)
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

@app.get("/", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/matcher", response_class=HTMLResponse)
async def matcher(
    request: Request,
    job_description: str = Form(...),
    resumes: List[UploadFile] = File(...)
):
    texts = []
    filenames = []

    for resume in resumes:
        path = os.path.join(UPLOAD_FOLDER, resume.filename)
        with open(path, "wb") as f:
            f.write(await resume.read())
        texts.append(extract_text(path))
        filenames.append(resume.filename)

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer().fit_transform([job_description] + texts)
    vectors = vectorizer.toarray()

    # Calculate cosine similarity
    job_vector = vectors[0]
    resume_vectors = vectors[1:]
    similarities = cosine_similarity([job_vector], resume_vectors)[0]

    top_indices = similarities.argsort()[-5:][::-1]
    top_resumes = [filenames[i] for i in top_indices]
    similarity_scores = [round(similarities[i], 2) for i in top_indices]

    return templates.TemplateResponse("index.html", {
        "request": request,
        "message": "Top matching resumes:",
        "top_resumes": top_resumes,
        "similarity_scores": similarity_scores
    })