from utils.inventory import load_inventory
from utils.filters import filter_products
from utils.llm_client import LLMClient


def main():

    # Load inventory
    inventory = load_inventory()

    # Get user query
    user_query = input("What kind of laptop are you looking for? ")

    # Convert user query → structured requirements
    llm = LLMClient(model_name="gemini-2.5-flash")

    user_requirements = llm.user_req_to_pydantic_model(
        user_query
    )

    print(user_requirements)

    # Filter inventory
    matching_products = filter_products(
        inventory,
        user_requirements
    )

    print(matching_products)


if __name__ == "__main__":
    main()