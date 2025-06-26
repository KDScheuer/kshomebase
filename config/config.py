# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # load from .env file, if present

class Config:
    LISTEN_ADDR = os.getenv("API_HOST", "127.0.0.1")
    LISTEN_PORT = os.getenv("API_PORT", "8000")
    DB_PATH = os.getenv("DB_PATH", "data/homebase.db")
    SCHEMA_PATH = os.getenv("SCHEMA_PATH", "data/schema.sql")