"""
Database configuration module.

This module initializes the SQLAlchemy engine and session factory
for the Task Manager application.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# SQLite local file path
DATABASE_URL = "sqlite:///./taskmanager.db"

# Needed for SQLite + threads
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Base class for SQLAlchemy declarative models."""

    pass


def get_db():
    """
    Provide a transactional scope around a series of operations.

    Yields:
        Session: The SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
