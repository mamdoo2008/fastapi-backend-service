from fastapi import FastAPI
app = FastAPI(title="FastAPI Backend Service")
@app.get("/")
def read_root():
return {"message": "Welcome to FastAPI Backend Service"}
@app.get("/health")
def health_check():
return {"status": "healthy"}
