"""
RAG chain logic.
WHY:
- Enforces strict grounding (zero hallucination)
- Clean separation from UI
- Deterministic and interview-safe
"""

from langchain.chains import RetrievalQA
from app.llm import get_llm
from app.retriever import get_retriever
from app.prompt import RAG_PROMPT


def build_rag_chain():
    """
    Builds a Retrieval-Augmented QA chain.

    Design choice:
    - RetrievalQA keeps retrieval + generation explicit
    - return_source_documents enables citations
    """
    return RetrievalQA.from_chain_type(
        llm=get_llm(),
        retriever=get_retriever(),
        chain_type="stuff",
        chain_type_kwargs={"prompt": RAG_PROMPT},
        return_source_documents=True
    )


def answer_question(question: str):
    """
    Answers a question strictly from retrieved PDF context.

    WHY:
    - Post-processing keeps UX clean
    - Core refusal logic remains enforced by the prompt
    """
    chain = build_rag_chain()
    result = chain(question)

    answer = result["result"].strip()
    source_docs = result.get("source_documents", [])

    # Collect unique page citations
    citations = sorted(
        {f"Page {doc.metadata.get('page', 'N/A')}" for doc in source_docs}
    )

    # UX cleanup ONLY (does not weaken guardrails)
    refusal_text = "I don't know based on the provided documents."
    if answer.endswith(refusal_text):
        answer = answer.replace(refusal_text, "").strip()

    if not answer:
        answer = refusal_text

    return answer, ", ".join(citations)
