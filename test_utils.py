from rag.retriever import retriever

question = input("Ask about your codebase: ")

docs = retriever.invoke(question)

print("\n========== RETRIEVED DOCUMENTS ==========\n")

for i, doc in enumerate(docs, 1):
    print(f"\n--- CHUNK {i} ---")
    print("SOURCE:", doc.metadata.get("source"))
    print("METADATA:", doc.metadata)
    print("CONTENT:")
    print(doc.page_content[:500])