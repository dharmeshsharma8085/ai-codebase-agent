from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from rag.retriever import retriever
from rag.prompt import prompt

load_dotenv()


llm = ChatOpenAI(
    model="gpt-5",
    temperature=1
)


question = input("Ask about your codebase: ")


# Get relevant code chunks
relevant_chunks = retriever.invoke(question)


# Create context
context = "\n\n".join(
    chunk.page_content
    for chunk in relevant_chunks
)


# Create final prompt
messages = prompt.invoke({
    "context": context,
    "question": question
})


# Generate answer
response = llm.invoke(messages)


print("\nAI:", response.content)