from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings
from database.models import Base

engine = create_engine(
    settings.DATABASE_URL,
    echo=False
)

# Create all tables if they don't exist
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_session():
    return SessionLocal()