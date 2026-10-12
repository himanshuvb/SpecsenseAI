from utils.inventory import load_inventory
from utils.filter_products import filter_products
from utils.llm_client import LLMClient
from utils.ranking import rank_products

def main():

    # Load inventory
    inventory = load_inventory()

    # Get user query
    user_query = input("What kind of laptop are you looking for? ")

    # Convert user query → structured requirements
    llm = LLMClient(model_name="gemini-3.5-flash")

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

    if matching_products.empty:
        alternatives = find_alternatives(inventory, user_requirements)
        # Display alternatives and explain their trade-offs
    else:
        ranked_products = rank_products(
            matching_products,
            user_requirements
        )
    # Display exact matches


if __name__ == "__main__":
    main()