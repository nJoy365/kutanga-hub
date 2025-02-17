from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from common.database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try: 
        db.execute("SELECT 1")
        return {"status": "OK", "database": "connected"}
    except Exception as e:
        return {"status": "ERROR", "database": str(e)}

@app.get("/")
def root():
    return {"message": "Game Server Service is running!"}