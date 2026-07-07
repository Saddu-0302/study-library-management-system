from fastapi import FastAPI
from app.api.router import api_router




app = FastAPI(
    title="Study Library Managment System",
    version="1.0.0"
)

app.include_router(api_router,prefix="/api/v1")

@app.get("/")
def root():
    return {"message":"Study Library Managment System API is running"}

