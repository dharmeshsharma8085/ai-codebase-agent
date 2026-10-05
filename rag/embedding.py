from langchain_openai import OpenAIEmbeddings
from rag.chunking import chunks


embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vectors = embedding_model.embed_documents(
    [chunk.page_content for chunk in chunks]
)

print("Total chunks:", len(chunks))
print("Total vectors:", len(vectors))
print("Vector dimensions:", len(vectors[0]))