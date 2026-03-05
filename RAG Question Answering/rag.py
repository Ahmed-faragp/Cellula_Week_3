
from langchain_community.vectorstores import FAISS
from openai import OpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains import RetrievalQA
from transformers import pipeline
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key
)


loader = TextLoader('./data.txt')
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
texts = text_splitter.split_documents(docs)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(texts, embeddings)
retriever = db.as_retriever(search_kwargs={"k": 5})
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template= """
You are answering questions about Ahmed.

Use ONLY the information from the context below.
If the answer is not  in the context, say:
I don't know.

Context:
{context}

Question: {question}

Answer:
""")
def ask_llm(prompt):

    response = client.chat.completions.create(
        model="meta-llama/llama-3-8b-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        max_tokens=200
    )

    return response.choices[0].message.content




def ask_question(query):
    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])

    prompt_text = prompt.format(context=context, question=query)
    answer = ask_llm(prompt_text)
    return answer, context