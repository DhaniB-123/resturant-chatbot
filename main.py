from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import chat

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://restaurant-booking-chatbot.vercel.app",
        "http://localhost:3000",  # local testing ke liye, optional
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
