# Resume ↔ Job Matcher (Streamlit, TF-IDF)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-brightgreen)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Srinivas-Malapati/Resume-Agent/blob/main/LICENSE)

Lightweight Streamlit app that matches resumes to job descriptions using **TF-IDF** and **cosine similarity**.  
Great as a starter project to learn classic NLP and build a simple HR assistant.

![demo](assets/screenshot-placeholder.png)

## ✨ Features
- Compare **resumes** and **job descriptions** from local JSONL files
- Compute **similarity scores** using `TfidfVectorizer` + `cosine_similarity`
- Select a job and see the **top-matching candidates**
- 100% local — no external services required

## 🛠 Tools & Libraries
- **Python**
- **Streamlit** (interactive UI)
- **scikit-learn** (`TfidfVectorizer`, `cosine_similarity`)
- **pandas** (data handling)
- Data format: **JSON Lines** (`.jsonl`)

## 🗂️ Repository Layout

```
.
├── app.py                         # Streamlit UI + matching logic
├── requirements.txt               # Dependencies
├── resumes/
│   └── resumes.jsonl             # Sample resumes (JSONL)
├── job_descriptions/
│   └── job_descriptions.jsonl    # Sample jobs (JSONL)
├── assets/
│   └── screenshot-placeholder.png
├── .gitignore
└── LICENSE
```

## 📄 Data Format (JSONL)

Each line is a JSON object.

**Example resume (`resumes/resumes.jsonl`)**
```json
{
  "id": "r1",
  "name": "Alex Chen",
  "summary": "Software engineer with 4 years of experience in Python, Streamlit, and ML.",
  "skills": ["Python", "Streamlit", "scikit-learn", "Pandas"],
  "experience": [{"title":"ML Engineer","company":"DataLeaf","years":2,"highlights":["Built TF-IDF pipelines"]}]
}
```

**Example job (`job_descriptions/job_descriptions.jsonl`)**
```json
{
  "id": "j1",
  "title": "ML App Engineer (Streamlit)",
  "company": "Quantiva",
  "description": "Build lightweight data apps with Streamlit and basic NLP.",
  "requirements": ["Python", "Streamlit", "scikit-learn"]
}
```

## 🧠 How It Works
1. **Load** resumes and job descriptions from JSONL files
2. **Preprocess** text fields (skills, summary, experience, description)
3. **Vectorize** with TF-IDF
4. **Compare** with cosine similarity → score in [0,1]
5. **Rank** and display candidates for the selected job

## 🔧 Next Steps / Improvements
- Add embeddings (`sentence-transformers`) for semantic matching
- Export results as CSV
- Weight certain fields more (e.g., skills)
- Replace placeholder screenshot with real UI

## 🛡️ License
This project is released under the **MIT License** — see [LICENSE](https://github.com/Srinivas-Malapati/Resume-Agent/blob/main/LICENSE).

## 👨‍💻 Credits
Created and maintained by **[Srinivas Malapati](https://github.com/Srinivas-Malapati)**