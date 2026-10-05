from rag.loader import load_repository

url = input("Repository URL: ")

documents = load_repository(url)

print("Loaded files:", len(documents))

for document in documents:
    print(document.metadata.get("source"))