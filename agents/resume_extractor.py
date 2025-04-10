import ollama

def extract_resume(resume_text):
    response = ollama.chat(model='llama3', messages=[
        {"role": "system", "content": "Extract skills, education, work experience, and certifications from this resume."},
        {"role": "user", "content": resume_text}
    ])
    return response['message']['content']
