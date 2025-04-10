import ollama

def summarize_jd(jd_text):
    response = ollama.chat(model='llama3', messages=[
        {"role": "system", "content": "Summarize the JD: Extract key skills, experience, qualifications, and responsibilities."},
        {"role": "user", "content": jd_text}
    ])
    return response['message']['content']
