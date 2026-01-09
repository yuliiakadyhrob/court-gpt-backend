from fastapi import FastAPI
from pydantic import BaseModel
from parser import search_court_case

app = FastAPI()

class SearchRequest(BaseModel):
    person: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/api/search")
def search(data: SearchRequest):
    results = search_court_case(data.person)

    if not results:
        return {"status": "not_found"}

    return {
        "status": "ok",
        "results": results
    }
