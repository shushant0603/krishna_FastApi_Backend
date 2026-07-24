from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from app.services.embedding import embeddings

# Load PDF
loader = PyPDFLoader("data/gita.pdf")
documents = loader.load()

print(f"Total Pages : {len(documents)}")

# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print(f"Total Chunks : {len(chunks)}")

# Create Vector Database
vector_db = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

# Save Locally
vector_db.save_local("vector_db")

print("✅ Vector Database Created Successfully!")