from gemini_service import ask_gemini


question = "What is Paracetamol used for?"

answer = ask_gemini(question)

print(answer)