from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

@app.get("/sugerir")
def sugerir():
    # Esta é a base da sua API
    return {"dezenas": [10, 22, 45, 67, 78]}
