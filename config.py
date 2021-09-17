import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), ".dev.env")
load_dotenv(env_path)

# vars have same name in dev and prod
FLASK_SECRET_KEY=os.getenv("FLASK_SECRET_KEY")
HERE_API_KEY=os.getenv("HERE_API_KEY")
REDIS_URL=os.getenv("REDIS_URL")
GEOCODE_URL=os.getenv("GEOCODE_URL")
GEOCODE_KEY=os.getenv("GEOCODE_KEY")
GEOCODE_SEARCH_PATH=os.getenv("GEOCODE_SEARCH_PATH")
GEOCODE_REVERSE_PATH=os.getenv("GEOCODE_REVERSE_PATH")