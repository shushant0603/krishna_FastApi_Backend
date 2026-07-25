from fastapi import FastAPI
from app.routes.chat import router
from fastapi.middleware.cors import CORSMiddleware
from app.routes.tts import router as tts_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
       "https://frontend-chat-with-krishna.vercel.app/"
    ],
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