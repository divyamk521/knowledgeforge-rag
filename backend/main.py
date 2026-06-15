from fastapi import FastAPI

from backend.routes.rag import router

app = FastAPI(
    title="KnowledgeForge API"
)


@app.get("/")
def home():

    return {
        "message": "KnowledgeForge API is running."
    }


app.include_router(router)