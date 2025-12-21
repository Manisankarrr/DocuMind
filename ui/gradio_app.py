"""
Gradio UI for PDF RAG Tutor.
WHY:
- Explicit file upload
- Deterministic storage
- Clean indexing flow
"""

import os
import shutil
import gradio as gr
from app.ingest import ingest_pdfs
from app.rag_chain import answer_question
from app.config import PDF_DIR


def upload_and_index(files):
    """
    Saves uploaded PDFs to data/pdfs/ and indexes them.
    """
    if not files:
        return "❌ No files uploaded."

    os.makedirs(PDF_DIR, exist_ok=True)

    for file in files:
        dest_path = os.path.join(PDF_DIR, os.path.basename(file.name))
        shutil.copy(file.name, dest_path)

    ingest_pdfs()
    return "✅ PDFs uploaded and indexed successfully."


def ask(question: str):
    if not question.strip():
        return "Please enter a question.", ""

    answer, sources = answer_question(question)
    return answer, sources


with gr.Blocks(title="PDF AI Tutor (Zero Hallucination)") as demo:
    gr.Markdown("## 📘 PDF-based AI Tutor")
    gr.Markdown(
        "• Upload PDFs\n"
        "• Index them explicitly\n"
        "• Ask questions answered **only** from documents"
    )

    pdf_files = gr.File(
        label="Upload PDFs",
        file_types=[".pdf"],
        file_count="multiple"
    )

    index_btn = gr.Button("📂 Upload & Index PDFs")
    status = gr.Textbox(label="Status", interactive=False)

    index_btn.click(upload_and_index, inputs=pdf_files, outputs=status)

    question = gr.Textbox(
        label="Ask a Question",
        placeholder="What is this document about?",
        lines=2
    )

    answer = gr.Textbox(
        label="Answer",
        lines=8,
        interactive=False
    )

    sources = gr.Textbox(
        label="Sources",
        lines=2,
        interactive=False
    )

    ask_btn = gr.Button("🔍 Ask")
    ask_btn.click(ask, inputs=question, outputs=[answer, sources])

demo.launch()
