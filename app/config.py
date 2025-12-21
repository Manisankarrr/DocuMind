"""
Central configuration.
WHY: Keeps provider choice abstract and swappable.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter (FREE)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = "mistralai/mistral-7b-instruct"

# Chunking
CHUNK_SIZE = 800
CHUNK_OVERLAP = 200

# Retrieval
TOP_K = 4

# Paths
PDF_DIR = "data/pdfs"
FAISS_DIR = "data/faiss_index"

# Local embeddings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
