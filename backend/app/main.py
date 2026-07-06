from fastapi import FastAPI

app = FastAPI(
    title="Study Library Managment System",
    version="1.0.0"
)
@app.get("/")
def root():
    return {"message":"Study Library Managment System API is running"}