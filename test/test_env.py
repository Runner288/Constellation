import os
from dotenv import load_dotenv
from libra.models.base_model import BaseModel

# Load variables from the .env file into the environment
load_dotenv()
print(".env is loaded")
# Access the variables using os.getenv()
python_path = os.getenv("PYTHONPATH")
api_key_alpha = os.getenv("API_KEY_ALPHA")
debug_mode = os.getenv("DEBUG", "False").lower() == "true"

# Example usage
print(f"PYTHONPATH: {python_path}")
print(f"API_KEY_ALPHA: {api_key_alpha}")
print(f"Debug Mode: {debug_mode}")
