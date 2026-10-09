from app.config import HF_TOKEN
from langchain_huggingface import HuggingFaceEndpointEmbeddings

if not HF_TOKEN:
    raise RuntimeError(
        "HF_TOKEN is missing. Add HF_TOKEN in Backend/.env to use Hugging Face embeddings."
    )

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    huggingfacehub_api_token=HF_TOKEN,
)