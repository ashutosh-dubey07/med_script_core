from gemini_service import ask_gemini

question = input("Ask your question: ")

answer = ask_gemini(question)

print("\nAnswer:\n")
print(answer)