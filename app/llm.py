"""
LLM via OpenRouter.
WHY: OpenRouter provides free hosted open-source models.
"""

from langchain_openai import ChatOpenAI
from app.config import OPENROUTER_API_KEY, OPENROUTER_MODEL


def get_llm():
    return ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
        model=OPENROUTER_MODEL,
        temperature=0,  # deterministic
    )
