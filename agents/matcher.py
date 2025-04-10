import ollama
from sklearn.metrics.pairwise import cosine_similarity

def get_embedding(text):
    response = ollama.embeddings(model='nomic-embed-text', prompt=text)
    return response['embedding']

def calculate_match_score(jd_summary, resume_summary):
    jd_emb = get_embedding(jd_summary)
    resume_emb = get_embedding(resume_summary)
    score = cosine_similarity([jd_emb], [resume_emb])[0][0] * 100
    return round(score, 2)
