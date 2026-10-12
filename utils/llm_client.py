from google import genai
import os

from models.requirements import UserRequirements
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from google.genai.errors import ServerError

load_dotenv()  # Load environment variables from .env file

class LLMClient:

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.client = genai.Client(
            api_key=os.environ.get("GEMINI_API_KEY")
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=3),
        retry=retry_if_exception_type(ServerError),
        reraise=True
    )    
    def user_req_to_pydantic_model(
        self,
        user_requirements: str
    ) -> UserRequirements:
        """
        Converts user requirements string to a Pydantic model.

        Args:
            user_requirements (str): User requirements in string format.

        Returns:
            UserRequirements: Pydantic model representing user requirements.
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=user_requirements,
            config={
                "response_mime_type": "application/json",
                "response_schema": UserRequirements
            }
        )

        # Assuming the response is a JSON string that can be parsed into the UserRequirements model
        return response.parsed