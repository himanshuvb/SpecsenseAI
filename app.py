
import streamlit as st

from utils.inventory import load_inventory
from utils.llm_client import LLMClient
from utils.filter_products import filter_products
from utils.ranking import rank_products


st.set_page_config(
    page_title="SpecSense AI",
    page_icon="💻",
    layout="wide"
)

st.title("💻 SpecSense AI")
st.caption("AI-powered laptop recommendations")

query = st.text_area(
    "What kind of laptop are you looking for?",
    placeholder="e.g. A laptop under ₹50,000, lightweight, with 16 GB RAM...",
    value=(
        "I need a laptop under ₹50,000, weighing at most "
        "1.5 kg, with at least 512 GB storage."
    ),
    height=100
)

if st.button("Find laptops", type="primary"):
    if not query.strip():
        st.warning("Please describe the laptop you want.")
    else:
        try:
            with st.spinner("Understanding your requirements..."):
                llm_client = LLMClient(
                    model_name="gemini-3.5-flash"
                )
                user_requirements = (
                    llm_client.user_req_to_pydantic_model(query)
                )

            if user_requirements is None:
                st.error("Could not understand your requirements. Please try again.")
                st.stop()

            st.subheader("Requirements understood")

            with st.expander("View extracted requirements"):
                st.json(user_requirements.model_dump())

            with st.spinner("Finding matching laptops..."):
                inventory = load_inventory()

                matching_products = filter_products(
                    inventory,
                    user_requirements
                )

            if matching_products.empty:
                st.warning(
                    "No laptops match all your requirements. "
                    "Try relaxing one or more constraints."
                )
            else:
                ranked_products = rank_products(
                    matching_products,
                    user_requirements
                )

                st.subheader(
                    f"Recommended laptops ({len(ranked_products)})"
                )

                display_columns = [
                    "name",
                    "price",
                    "weight_kg",
                    "ram_gb",
                    "storage_gb",
                    "battery_hours",
                    "processor"
                ]

                available_columns = [
                    column
                    for column in display_columns
                    if column in ranked_products.columns
                ]

                st.dataframe(
                    ranked_products[available_columns],
                    hide_index=True,
                    use_container_width=True
                )

                st.caption(
                    "Products are ranked using your active preferences. "
                    "Scores are relative to the matching products."
                )

        except Exception as error:
            st.error(
                "Something went wrong while generating recommendations."
            )
            st.exception(error)