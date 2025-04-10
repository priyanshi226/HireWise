# test_agents.py

from jd_summarizer import summarize_jd
from resume_extractor import extract_resume
from matcher import calculate_match_score

# Load your sample data
with open("../JD.txt", "r", encoding="ISO-8859-1") as f:
    jd_text = f.read()

with open("../Resume.pdf", "r", encoding="ISO-8859-1") as f:
    resume_text = f.read()

# Step 1: Summarize JD
jd_summary = summarize_jd(jd_text)
print("=== JD SUMMARY ===")
print(jd_summary)

# Step 2: Extract Resume Info
resume_summary = extract_resume(resume_text)
print("\n=== RESUME EXTRACTED INFO ===")
print(resume_summary)

# Step 3: Calculate Match Score
score = calculate_match_score(jd_summary, resume_summary)
print(f"\n=== MATCH SCORE: {score}% ===")
