
import streamlit as st
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- Load datasets (adjust path if needed) ---
RESUMES_FILE = "resumes/resumes.jsonl"
JDS_FILE = "job_descriptions/job_descriptions.jsonl"

def load_jsonl(path):
    items = []
    with open(path, "r") as f:
        for line in f:
            items.append(json.loads(line))
    return items

resumes = load_jsonl(RESUMES_FILE)
jds = load_jsonl(JDS_FILE)

# --- Helpers ---
def resume_text(r):
    skills = " ".join(r.get("skills", []))
    exp = " ".join([e["title"] + " " + e["company"] for e in r.get("experience", [])])
    return f"{r['summary']} {skills} {exp} {r['education']}"

def jd_text(jd):
    return jd["title"] + " " + jd["description"]

resume_texts = [resume_text(r) for r in resumes]
jd_texts = [jd_text(jd) for jd in jds]

# --- UI ---
st.title("Autonomous HR Agent – Demo")

jd_titles = [jd["title"] for jd in jds]
choice = st.selectbox("Select a Job Description", jd_titles)

if st.button("Find Matching Resumes"):
    jd_idx = jd_titles.index(choice)
    jd_selected = jds[jd_idx]
    jd_vec = [jd_texts[jd_idx]]

    # TF-IDF similarity
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(resume_texts + jd_vec)
    resume_vecs = X[:-1]
    jd_vec = X[-1]

    sims = cosine_similarity(resume_vecs, jd_vec.reshape(1, -1)).flatten()
    ranked = sorted(zip(resumes, sims), key=lambda x: x[1], reverse=True)

    # --- Show JD text ---
    st.subheader("Job Description")
    st.markdown(f"**{jd_selected['title']}** – {jd_selected['location']} ({jd_selected['level']})")
    st.write(jd_selected["description"])

    # --- Show candidates ---
    st.subheader("Top Candidates")
    for r, score in ranked[:5]:
        with st.expander(f"{r['name']} – {round(score*100,2)}% match"):
            st.markdown(f"**Email:** {r['email']}  \n"
                        f"**Location:** {r['location']}  \n"
                        f"**Experience:** {r['years_experience']} years  \n"
                        f"**Education:** {r['education']}")
            
            st.markdown("**Top Skills:**")
            st.write(", ".join(r["skills"]))

            st.markdown("**Summary:**")
            st.write(r["summary"])

            st.markdown("**Experience:**")
            for e in r["experience"]:
                st.write(f"- {e['title']} @ {e['company']} ({e['years']} yrs)")
                for h in e["highlights"]:
                    st.write(f"  • {h}")
