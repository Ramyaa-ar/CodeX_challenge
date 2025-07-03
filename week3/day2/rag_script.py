# rag_script.py

from langchain_community.llms import Ollama
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
import os

# === STEP 1: Load your text files ===
print("🔎 Loading text files from data folder...")

folder_path = r"C:\Users\ramya\Documents\codex\week3\day2\data"

documents = []
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        loader = TextLoader(os.path.join(folder_path, filename), encoding='utf-8')
        documents.extend(loader.load())

print(f"✅ Loaded {len(documents)} document chunks.")

# === STEP 2: Split into smaller chunks ===
print("✂️ Splitting text into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# === STEP 3: Create embeddings (updated) ===
print("✨ Creating embeddings...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# === STEP 4: Store vectors in Chroma ===
print("💾 Storing embeddings in local Chroma DB...")
vectorstore = Chroma.from_documents(docs, embeddings)

# === STEP 5: Create retriever ===
retriever = vectorstore.as_retriever()

# === STEP 6: Load local LLM via Ollama ===
print("🤖 Loading local model (Ollama)...")
llm = Ollama(model="llama2")

# === STEP 7: Build RAG chain ===
rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")

# === STEP 8: Ask your question ===
query = "Summarize the main points from my notes."
print(f"💬 Question: {query}")

answer = rag_chain.run(query)

print("\n✅ === ANSWER ===")
print(answer)
