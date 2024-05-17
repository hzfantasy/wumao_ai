from langchain_openai import ChatOpenAI
# from langchain_ex.chat_models import ChatOpenAI
from langchain_ex.config import config


llm = ChatOpenAI(
    openai_api_base="https://api.moonshot.cn/v1",
    openai_api_key=config.kimi_token,
    model_name="moonshot-v1-8k",
)

print(llm.invoke("how can langsmith help with testing?"))
