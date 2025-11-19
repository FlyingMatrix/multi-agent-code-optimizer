from dotenv import load_dotenv
import os

load_dotenv()  # Automatically loads .env once
MODEL = os.getenv("MODEL")