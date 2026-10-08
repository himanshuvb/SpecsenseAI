from google import genai
import os

from models.requirements import UserRequirements


class LLMClient:

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.client = genai.Client(
            api_key=os.environ.get("GEMINI_API_KEY")
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
        response = self.client.generate_text(
            model=self.model_name,
            content=user_requirements,
            config={
                "response_mime_type": "application/json",
                "response_schema": UserRequirements
            }
        )

        # Assuming the response is a JSON string that can be parsed into the UserRequirements model
        return response.parsed