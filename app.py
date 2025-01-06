from fastapi import FastAPI
from pydantic import BaseModel
from better_profanity import profanity
import re
import logging

# Initialize FastAPI app
app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def sanitize_input(text: str) -> str:
    """
    Sanitize input text by removing control characters.

    Args:
        text (str): The input text to sanitize.

    Returns:
        str: The sanitized text with control characters removed.
    """
    return re.sub(r'[\x00-\x1F\x7F]', '', text)

# Pydantic model for input validation
class InputText(BaseModel):
    input_text: str

# Load profanity words using better_profanity library
profanity.load_censor_words()

@app.get("/")
async def root():
    """
    Basic endpoint to confirm the app is running.

    Returns:
        dict: A message indicating that the API is running.
    """
    return {"message": "Welcome to the Profanity Censor API!"}

@app.post("/censor/")
async def censor_text(input_data: InputText):
    """
    Censor profanity words in the input text.

    Args:
        input_data (InputText): The input data containing text to be censored.

    Returns:
        dict: The censored version of the input text.
    """
    # Sanitize the input text
    input_text = sanitize_input(input_data.input_text)
    logger.debug(f"Sanitized input text: {input_text}")

    # Censor the text
    censored_text = profanity.censor(input_text)

    # Return the censored text
    return {"censored_text": censored_text}































