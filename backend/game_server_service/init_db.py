from common.database import Base, engine


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Tables initialized successfully.")


if __name__ == "__main__":
    init_db()
