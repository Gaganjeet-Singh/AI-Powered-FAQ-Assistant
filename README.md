# 📘 AI-Powered FAQ Assistant  

An interactive **AI-powered assistant** built with **LangChain, FAISS, HuggingFace embeddings, and Google Gemini** that answers frequently asked questions (FAQs) from a structured knowledge base (`faq.csv`).  

This project demonstrates how to:  
- Convert FAQ data into embeddings.  
- Store and query them efficiently using **FAISS**.  
- Use a **retrieval-based question answering chain** with **custom prompts**.  
- Serve a simple **Streamlit UI** for user interaction.  

---

## 🗂️ Project Structure  

AI-Powered-FAQ-Assistant/
│
├── main.py # Streamlit app (UI)
├── langchain_helper.py # Backend logic (LLM, embeddings, FAISS, QA chain)
├── faq.csv # FAQ dataset
├── faiss_index/ # Vector database (auto-created)
├── assets/ # Screenshots & UI images
│ └── ui_demo.png # Example Streamlit interface screenshot
├── .env # Stores GOOGLE_API_KEY
└── README.md # Project documentation

## ⚡ Features  

✅ Converts CSV-based FAQs into embeddings with HuggingFace.  
✅ Stores & retrieves FAQs efficiently using FAISS.  
✅ Uses **Google Gemini** via LangChain for response generation.  
✅ Custom prompt ensures **answers only come from knowledge base**.  
✅ Falls back to **“I don't know.”** when answer is not found.  
✅ Streamlit-based UI for a simple **Q&A chat experience**. 

## 🔧 Setup Instructions  

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/AI-Powered-FAQ-Assistant.git
cd AI-Powered-FAQ-Assistant
2️⃣ Install dependencies
Make sure you have Python 3.9+ installed. Then install required libraries:

bash
Copy code
pip install streamlit langchain langchain-community langchain-huggingface langchain-google-genai faiss-cpu python-dotenv
3️⃣ Set up environment variables
Create a .env file in the project root and add your Google API key:

ini
Copy code
GOOGLE_API_KEY=your_api_key_here
4️⃣ Run the Streamlit app
bash
Copy code
streamlit run main.py
🎯 Usage
Type a question (e.g., "How can I reset my password?") in the input box.

The assistant will retrieve the most relevant FAQ from the database and answer.

If the answer isn’t available in the knowledge base, it will reply with:

rust
Copy code
I don't know.
📊 Dataset Example (codebasics_faqs.csv)
Question	Answer
How can I reset my password?	Go to the login page and click on 'Forgot Password'...
Can I track my order?	Yes, you can track your order by visiting the 'My Orders' section...
What payment methods are accepted?	We accept credit/debit cards, UPI, net banking, and wallets...
Do you ship internationally?	Currently, we only ship within India, but international shipping soon.
...	...

🚀 Tech Stack
LangChain → Chains, memory, prompt templates

Google Gemini → LLM backend

HuggingFace → Embeddings (all-mpnet-base-v2)

FAISS → Vector database for semantic search

Streamlit → Web-based UI

dotenv → Manage environment variables