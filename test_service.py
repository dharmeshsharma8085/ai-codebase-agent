from services.codebase_service import ask_codebase


question = input("Ask your codebase: ")

response = ask_codebase(question)

print("\n================ AI RESPONSE ================\n")
print(response)