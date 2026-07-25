import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from fastapi import FastAPI
from app.routes.chat import router
from fastapi.middleware.cors import CORSMiddleware
from app.routes.tts import router as tts_router


origins = [
    "http://localhost:5173",
    os.getenv("FRONTEND_URL"),
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
      allow_origins=[origin for origin in origins if origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(tts_router)
# app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Backend Running 🚀"
    }