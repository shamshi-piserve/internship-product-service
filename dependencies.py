from database import SessionLocal  # Absolute import

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()