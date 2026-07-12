from gemini_service import ask_gemini
from search_db import search_medicine

question = input("Ask your question: ")
medicine = search_medicine(question)
if medicine:
    print("\nMedicine Found\n")

print("Brand Name:", medicine[1])
print("Generic Name:", medicine[2])
if medicine[3] == 1:
    print("Prescription Required: Yes")
else:
    print("Prescription Required: No")

answer = ask_gemini(question)

print("\nAnswer:\n")
print(answer)