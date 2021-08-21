import os
from dotenv import load_dotenv

## load development environment variables from .env
env_path = os.path.join(os.path.dirname(__file__), ".dev.env")
load_dotenv(env_path)

is_prod = os.environ.get("ON_HEROKU")

# load correct values based on production or not
if is_prod:
    FLASK_SECRET_KEY=os.environ.get("FLASK_SECRET_KEY")
    HERE_API_KEY=os.environ.getenv("HERE_API_KEY")
    REDIS_URL=os.getenv("REDIS_URL")
else:
    FLASK_SECRET_KEY=os.getenv("FLASK_SECRET_KEY")
    REDIS_URL=os.getenv("REDIS_URL")
    HERE_API_KEY=os.getenv("HERE_API_KEY")