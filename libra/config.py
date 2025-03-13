import os
from dotenv import load_dotenv

# Load variables from the .env file into the environment
load_dotenv()

# Access the variables using os.getenv()
PYTHONPATH = os.getenv("PYTHONPATH")
API_KEY_ALPHA = os.getenv("API_KEY_ALPHA")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

