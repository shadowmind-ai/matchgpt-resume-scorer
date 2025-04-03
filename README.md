<!-- Hero Banner -->
<p align="center" style="margin-bottom: 10px;">
  <img src="assets/matchgpt_hero.png" alt="Visual overview: Resume + JD ➡️ GPT ➡️ Match Score" width="800"/>
</p>

<h1 align="center">MatchGPT 💼📊</h1>
<h3 align="center">AI-Powered Resume & Job Description Scoring</h3>

<p align="center">
  ✨ Score how well a resume fits a job description using GPT-powered analysis and structured insights.
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="#"><img src="https://img.shields.io/badge/Powered%20By-GPT4-blueviolet" alt="Powered by GPT-4"></a>
  <a href="#"><img src="https://img.shields.io/badge/Frontend-React-informational" alt="Frontend: React" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Backend-FastAPI-green" alt="Backend: FastAPI" /></a>
</p>

---

## 🚀 About

**MatchGPT** is an open-source tool that uses LLMs to assess how well a candidate's resume matches a job description — giving back structured scores, fit summaries, and improvement suggestions.

Whether you're a job seeker, recruiter, or building hiring tools, MatchGPT helps you **automate alignment insights** using explainable AI.

---

## 🎥 Demo

> 🔄 Replace the GIF below with a short screen recording or animated walkthrough of MatchGPT in action.

<p align="center" style="margin-bottom: 10px;">
  <img src="assets/demo_scoring.gif" alt="Demo of MatchGPT scoring a resume against a job description" width="700"/>
</p>

---

## ✨ Features

| Feature                          | Description                                                     |
| -------------------------------- | --------------------------------------------------------------- |
| ✅ **GPT Scoring Engine**        | Uses OpenAI to evaluate resume-to-JD fit with structured rubric |
| 📄 **Natural Language Feedback** | Explains match gaps, missing keywords, and strengths            |
| 📊 **Structured Output**         | Outputs JSON score, strengths, gaps, and suggestions            |
| 🔍 **RAG-Compatible**            | Easily extendable to include knowledge base or skill ontology   |
| ⚙️ **Modular Backend**           | Built with Python (FastAPI/Flask), easily testable and scalable |
| 🌐 **React Frontend**            | Clean UI for uploading files and displaying match results       |

---

## 🛠 How It Works

<!--
<p align="center" style="margin-bottom: 10px;">
  <img src="assets/how_it_works.png" alt="Diagram of how MatchGPT processes resume and job description into a match score" width="750"/>
</p>
-->

> 💡 _Diagram flow:_
>
> - Resume Upload 📝
> - Job Description 📄
> - ➡️ Passed to GPT with a custom prompt
> - ➡️ Returned: Score (0–100), Gaps, Suggestions
> - ➡️ Displayed in the UI

---

## 🧱 Tech Stack

| Layer               | Tech                        |
| ------------------- | --------------------------- |
| **Frontend**        | React / Next.js             |
| **Backend**         | Python + FastAPI (or Flask) |
| **AI**              | OpenAI GPT (or local LLMs)  |
| **Storage**         | Local / Supabase (optional) |
| **Styling**         | Tailwind / CSS Modules      |
| **Auth (optional)** | Clerk / Auth0 / Firebase    |

---

## 🧪 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/matchgpt-resume-scorer.git
cd matchgpt-resume-scorer
```

### 🛠️ 2. Set Up the Backend

```bash
# Step into the backend directory
cd backend

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn

# Run the FastAPI server
uvicorn app.main:app --reload
```

Test the health endpoint:  
[http://localhost:8000/health](http://localhost:8000/health)  
→ Expected response: `{"status": "ok"}`

Open the Swagger UI:  
[http://localhost:8000/docs](http://localhost:8000/docs)
