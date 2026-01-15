from fastapi import FastAPI

app = FastAPI()

notes = [
    {"id": 1, "title": "First note"},
    {"id": 2, "title": "Second note"}
]

@app.get("/")
def root():
    return {"status": "Notes API is running"}

@app.get("/notes")
def get_notes():
    return notes



