
# from app.config import HF_TOKEN
from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY


# llm = HuggingFaceEndpoint(
#     repo_id="Qwen/Qwen2.5-7B-Instruct",
#     task="text-generation",
#     huggingfacehub_api_token=HF_TOKEN,

#     max_new_tokens=512,
#     temperature=0.3,
# )

llm=ChatGroq(
     model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    temperature=0.3,
)




# model=ChatHuggingFace(llm=llm)




def ask_llm(question: str):
    response = llm.invoke(question)
    return response.content