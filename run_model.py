import ollama
model_name = "mistral"
prompt = "Explain what Agent AI is in simple words."
response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
print("AI Response:", response["message"]["content"])