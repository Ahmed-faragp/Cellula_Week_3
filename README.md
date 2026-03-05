# Ahmed Farag AI Assistant (RAG System)

A simple **Retrieval-Augmented Generation (RAG)** application that answers questions about **Ahmed Farag** using a local knowledge base, FAISS vector search, and an LLM accessed through **OpenRouter**.

The system retrieves relevant information from a document and uses a language model to generate accurate answers based only on that context.

---

# Features

* Retrieval-Augmented Generation (RAG)
* FAISS vector database for similarity search
* HuggingFace sentence-transformer embeddings
* OpenRouter LLM integration
* Streamlit web interface
* Local knowledge base (`data.txt`)
* Secure API key handling using `.env`

---

# Project Structure

```
project/
│
├── app.py              # Streamlit user interface
├── rag_system.py       # RAG pipeline (retrieval + LLM)
├── data.txt            # Knowledge base about Ahmed Farag
├── requirements.txt    # Python dependencies
├── .env                # API key (NOT uploaded to GitHub)
└── README.md
```

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

Create a virtual environment (recommended):

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# API Key Setup (Important)

This project uses **OpenRouter** to access the LLM.

You must create a `.env` file in the project root and add your API key.

Create a file named:

```
.env
```

Add the following:

```
OPENROUTER_API_KEY=your_api_key_here
```

Example:

```
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxx
```

The application loads this key automatically using `python-dotenv`.

⚠️ **Never commit your API key to GitHub.**

Make sure `.env` is included in `.gitignore`.

Example `.gitignore`:

```
.env
__pycache__/
*.pyc
```

---

# Running the Application

Start the Streamlit app:

```
streamlit run app.py
```

Your browser will open automatically:

```
http://localhost:8501
```

You can now ask questions about Ahmed Farag.

Example questions:

* What is Ahmed Farag studying?
* What programming language does Ahmed prefer?
* What projects is Ahmed working on?
* What companies does Ahmed want to work for?
* Give me a brief about Ahmed Farag.

---

# Technologies Used

* Python
* Streamlit
* LangChain
* FAISS
* HuggingFace sentence-transformers
* OpenRouter API
* Retrieval-Augmented Generation (RAG)

---

# How the System Works

1. The document (`data.txt`) is loaded and split into chunks.
2. Each chunk is converted into embeddings using a sentence-transformer model.
3. The embeddings are stored in a FAISS vector database.
4. When a user asks a question:

   * Relevant chunks are retrieved using similarity search.
   * The retrieved context is passed to the LLM.
   * The LLM generates an answer based only on the retrieved information.

---

# Example Workflow

```
User Question
     ↓
Retriever (FAISS)
     ↓
Relevant Context
     ↓
LLM (OpenRouter)
     ↓
Generated Answer
```

---

# Notes

* This project is a **simple educational implementation of a RAG system**.
* It is designed as a **portfolio project for AI / ML engineering**.
* The knowledge base can easily be extended with additional documents.

---

# License

This project is open-source and free to use for educational purposes.
# Ahmed Farag AI Assistant (RAG System)

A simple **Retrieval-Augmented Generation (RAG)** application that answers questions about **Ahmed Farag** using a local knowledge base, FAISS vector search, and an LLM accessed through **OpenRouter**.

The system retrieves relevant information from a document and uses a language model to generate accurate answers based only on that context.

---

# Features

* Retrieval-Augmented Generation (RAG)
* FAISS vector database for similarity search
* HuggingFace sentence-transformer embeddings
* OpenRouter LLM integration
* Streamlit web interface
* Local knowledge base (`data.txt`)
* Secure API key handling using `.env`

---

# Project Structure

```
project/
│
├── app.py              # Streamlit user interface
├── rag_system.py       # RAG pipeline (retrieval + LLM)
├── data.txt            # Knowledge base about Ahmed Farag
├── requirements.txt    # Python dependencies
├── .env                # API key (NOT uploaded to GitHub)
└── README.md
```

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

Create a virtual environment (recommended):

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# API Key Setup (Important)

This project uses **OpenRouter** to access the LLM.

You must create a `.env` file in the project root and add your API key.

Create a file named:

```
.env
```

Add the following:

```
OPENROUTER_API_KEY=your_api_key_here
```

Example:

```
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxx
```

The application loads this key automatically using `python-dotenv`.

---

# Running the Application

Start the Streamlit app:

```
streamlit run app.py
```

Your browser will open automatically:

```
http://localhost:8501
```

You can now ask questions about Ahmed Farag.

Example questions:

* What is Ahmed Farag studying?
* What programming language does Ahmed prefer?
* What projects is Ahmed working on?
* What companies does Ahmed want to work for?
* Give me a brief about Ahmed Farag.

---

# Technologies Used

* Python
* Streamlit
* LangChain
* FAISS
* HuggingFace sentence-transformers
* OpenRouter API
* Retrieval-Augmented Generation (RAG)

---

# How the System Works

1. The document (`data.txt`) is loaded and split into chunks.
2. Each chunk is converted into embeddings using a sentence-transformer model.
3. The embeddings are stored in a FAISS vector database.
4. When a user asks a question:

   * Relevant chunks are retrieved using similarity search.
   * The retrieved context is passed to the LLM.
   * The LLM generates an answer based only on the retrieved information.

---

# Example Workflow

```
User Question
      ↓
Embedding Model
(all-MiniLM-L6-v2)
      ↓
Vector Search
(FAISS)
      ↓
Relevant Context
      ↓
LLM
(Llama-3-8B-Instruct via OpenRouter)
      ↓
Generated Answer
```

---
Why These Models Were Chosen

all-MiniLM-L6-v2

Lightweight

Fast

Strong semantic similarity performance

Commonly used for RAG retrieval systems

Llama-3-8B-Instruct

Strong instruction-following capability

Good balance between quality and cost

Accessible through OpenRouter
# Notes

* This project is a **simple educational implementation of a RAG system**.
* It is designed as a **portfolio project for AI / ML engineering**.
* The knowledge base can easily be extended with additional documents.

---


