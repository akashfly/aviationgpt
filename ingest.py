import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings


DATA_PATH = "data"
DB_FAISS_PATH = "vectorstore"


def load_pdfs():
    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(DATA_PATH, file)

            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())

    return documents


def create_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    texts = splitter.split_documents(documents)
    return texts


def create_vectorstore(texts):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(texts, embeddings)

    db.save_local(DB_FAISS_PATH)


if __name__ == "__main__":
    print("Loading PDFs...")

    docs = load_pdfs()

    print(f"Loaded {len(docs)} pages")

    chunks = create_chunks(docs)

    print(f"Created {len(chunks)} chunks")

    create_vectorstore(chunks)

    print("Vector DB saved successfully")