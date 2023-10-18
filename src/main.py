from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_root():
    """Says Hello"""
    return {"message": "Hello, World!"}
