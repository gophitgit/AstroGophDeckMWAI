# source\astrodeck\config.py
import os
from dotenv import load_dotenv

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")

if not NASA_API_KEY:
    raise RuntimeError(
        "NASA_API_KEY not configured"
        "Check README.md for more information"
    )
