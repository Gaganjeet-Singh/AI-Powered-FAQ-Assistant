from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

llm = ChatGoogleGenerativeAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-1.5-flash",
    temperature=0.3
)

# Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# Path for FAISS index
vector_file_path = "faiss_index"


def create_vector_db():
    """Create FAISS vector database from FAQ CSV."""
    loader = CSVLoader(file_path="faq.csv", source_column="prompt")
    data = loader.load()
    vectordb = FAISS.from_documents(documents=data, embedding=embeddings)
    vectordb.save_local(vector_file_path)


def get_qa_chain():
    """Load FAISS vector DB and create RetrievalQA chain."""
    vectordb = FAISS.load_local(vector_file_path, embeddings, allow_dangerous_deserialization=True)
    retriever = vectordb.as_retriever(score_threshold=0.7)

    # Prompt
    prompt_template = """
    Given the following context and a question, generate an answer based only on this context.
    In the answer, try to provide as much text as possible from the "response" section in the source document context without making unnecessary changes.
    If the answer is not found in the context, reply strictly with: "I don't know."

    CONTEXT: {context}

    QUESTION: {question}
    """
    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    # Chain
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        input_key="query",
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )
    return chain
