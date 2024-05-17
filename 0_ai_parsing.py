import asyncio
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    openai_api_base="https://api.moonshot.cn/v1",
    openai_api_key="sk-24F4Er7oYAOzG7CMhgnkeE47NGxa4u5JDPcT0nXq34xVGz1y",
    model_name="moonshot-v1-8k",
)