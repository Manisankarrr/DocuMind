# DocuMind

```markdown
# 🧠 DocuMind

**DocuMind** is a PDF Query Resolver powered by Retrieval-Augmented Generation (RAG). Upload PDFs and ask questions—DocuMind will fetch precise, grounded answers using local embeddings, eliminating hallucinations and unnecessary API costs.

---

## 🚀 Introduction

DocuMind enables users to upload PDF documents and interact with them via natural language queries. It leverages free open-source LLMs through OpenRouter, local vector search (FAISS), and strict prompting to ensure every answer is grounded in your documents. If your question can't be answered from the data, DocuMind will tell you—no guessing, no hallucination.

---

## ✨ Features

- 📄 **PDF Upload & Ingestion**: Easily upload and index your PDFs.
- 🧩 **Local Vector Embeddings**: All retrieval is handled locally, no paid APIs required.
- 🤖 **Open-source LLMs via OpenRouter**: Uses free, hosted language models.
- 🛡 **Strict RAG Prompting**: Eliminates hallucination; only answers from your data.
- 💡 **Simple Gradio UI**: User-friendly web interface for uploads and queries.

---

## ⚡ Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/DocuMind.git
    cd DocuMind
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your environment variables:**
    - Copy `.env.example` to `.env` and fill in your `OPENROUTER_API_KEY`.

---

## 🎯 Usage

1. **Start the Gradio UI:**
    ```sh
    python ui/gradio_app.py
    ```

2. **In your browser:**
    - Upload your PDFs.
    - Ask questions about your documents.
    - Instantly receive factually-grounded answers.

---

## 🛠 File Structure

```
DocuMind/
├── app/
│   ├── __init__.py
│   ├── config.py          # Central configuration
│   ├── ingest.py          # PDF ingestion & embedding
│   ├── llm.py             # OpenRouter LLM interface
│   ├── prompt.py          # Strict RAG prompting
│   ├── rag_chain.py       # RAG chain logic
│   ├── retriever.py       # Vector retrieval
├── ui/
│   ├── __init__.py
│   ├── gradio_app.py      # Gradio-based UI
├── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -am 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> **DocuMind**: Query your PDFs with confidence—no hallucinations, just facts.
```


## License
This project is licensed under the **Apache-2.0** License.

---
🔗 GitHub Repo: https://github.com/Manisankarrr/DocuMind