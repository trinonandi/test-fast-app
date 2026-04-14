from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"message": "Hello, FastAPI with uv!"}


@app.get("/")
def core():
    return {"message": "This is the core endpoint"}