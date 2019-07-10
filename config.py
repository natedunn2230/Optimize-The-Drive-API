import os
from dotenv import load_dotenv

## load development environment variables from .env
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

is_prod = os.environ.get("ON_HEROKU")

GOOGLE_API_KEY = ""
FLASK_SECRET_KEY=""

# load correct values based on production or not
if is_prod:
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    FLASK_SECRET_KEY=os.environ.get("FLASK_SECRET_KEY")
    REDISTOGO_URL=os.getenv("REDISTOGO_URL")
else:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    FLASK_SECRET_KEY=os.getenv("FLASK_SECRET_KEY")
    REDISTOGO_URL=os.getenv("REDISTOGO_URL")