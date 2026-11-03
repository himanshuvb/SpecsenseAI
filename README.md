# 💻 SpecSense AI

**AI-powered laptop recommendations using natural language.**

SpecSense AI helps users find suitable laptops by translating
natural-language requirements into structured constraints, filtering a
product inventory, and ranking matching products according to their
preferences.

## Project Overview

Finding the right laptop can be difficult when users have different
budgets, hardware requirements, and personal preferences.

SpecSense AI lets users describe the laptop they want in plain English.
Google Gemini extracts structured requirements, Pydantic represents
those requirements, and Pandas filters and ranks products from a local
laptop inventory.

## Key Features

-   **Natural-language requirement extraction** using the Google Gemini
    API.
-   **Structured requirements** represented with Pydantic.
-   **Hard-constraint filtering** for budget, weight, RAM, storage, and
    battery life.
-   **Preference-based ranking** using normalized scores and weighted
    priorities.
-   **Missing-constraint handling** so unspecified numerical
    requirements do not filter out products.
-   **No-match handling** when no products satisfy all specified hard
    constraints.
-   **Streamlit web interface** for entering queries and viewing
    recommendations.
-   **Modular codebase** separating requirement extraction, inventory
    loading, filtering, ranking, and validation.

## Tech Stack

-   Python
-   Google Gemini API
-   `google-genai`
-   Pydantic
-   Pandas
-   Streamlit
-   `python-dotenv`
-   Tenacity

## Project Structure

``` text
specsense/
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── models/
│   └── requirements.py
├── utils/
│   ├── inventory.py
│   ├── llm_client.py
│   ├── filter_products.py
│   ├── ranking.py
│   └── validate_requirements.py
├── inventory/
│   └── inventory.json
└── screenshots/
    ├── recommendations.png
    ├── extracted-requirements.png
    └── no-match.png
```

This is the intended structure. Keep only the files and screenshots that
exist in your repository.

## Setup Instructions

### 1. Prerequisites

-   Python installed
-   A Google Gemini API key

### 2. Clone the repository

``` bash
git clone https://github.com/himanshuvb/SpecsenseAI.git
cd SpecsenseAI
```

### 3. Create and activate a virtual environment

On Windows PowerShell:

``` powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the virtual environment's Python
executable directly.

### 4. Install dependencies

``` powershell
py -m pip install -r requirements.txt
```

If `requirements.txt` has not been created yet, install the current
dependencies:

``` powershell
py -m pip install google-genai pandas pydantic streamlit python-dotenv tenacity
```

### 5. Configure the API key

Create a `.env` file in the project root:

``` env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own key. Never commit `.env` or expose
the API key in screenshots or source code.

### 6. Configure the Gemini model

Ensure the model identifier used in `app.py` is available to your Gemini
API key. For example, keep the same model identifier that currently
works in your environment:

``` python
llm_client = LLMClient(model_name="YOUR_WORKING_GEMINI_MODEL")
```

### 7. Run the application

Launch the Streamlit interface from the project root:

``` powershell
py -m streamlit run app.py
```

To run the command-line version:

``` powershell
py main.py
```

## How It Works

1.  **User input:** The user describes laptop requirements in natural
    language.
2.  **Requirement extraction:** Gemini converts the query into a
    structured Pydantic model.
3.  **Inventory loading:** Pandas loads the product inventory from JSON
    and flattens nested specifications.
4.  **Constraint filtering:** The filtering module selects products that
    satisfy the specified hard constraints.
5.  **Preference scoring:** The ranking module normalizes supported
    numerical attributes.
6.  **Weighted ranking:** Active preference scores are combined using
    their priorities.
7.  **Result display:** Streamlit displays matching products or a
    no-match message.

### Architecture

``` text
User Query
    |
    v
Google Gemini API
    |
    v
UserRequirements (Pydantic)
    |
    v
Load Inventory (Pandas)
    |
    v
Filter Products
    |
    v
Rank Matching Products
    |
    v
Display Recommendations (Streamlit)
```

## Ranking Approach

The current ranking implementation supports numerical preferences such
as laptop weight and battery life.

-   Lower weight receives a higher weight score.
-   Higher battery life receives a higher battery score.
-   Active scores are combined according to their priorities.
-   Products are sorted by recommendation score in descending order.

The weighted score is:

\[ `\text{Score}`{=tex} =
`\frac{\sum_i (\text{Preference Score}_i \times \text{Priority}_i)}`{=tex}
{`\sum`{=tex}\_i `\text{Priority}`{=tex}\_i} \]

Scores are relative to the filtered candidate set, not universal
product-quality ratings.

## Example Queries

**Budget and storage**

> I need a laptop under ₹50,000 with at least 512 GB storage.

**Lightweight laptop**

> I need a laptop under ₹50,000, weighing at most 1.5 kg, with at least
> 512 GB storage.

**Multiple constraints**

> I need a laptop under ₹50,000, weighing at most 1.5 kg, with at least
> 16 GB RAM, 512 GB storage, and at least 8 hours of battery life.

**Test the no-match case**

> I need a laptop under ₹5,000, weighing at most 0.5 kg, with at least
> 128 GB RAM, 10 TB storage, and at least 50 hours of battery life.

## Demo Screenshots

Add screenshots of the running application to the `screenshots/`
directory. Update these filenames to match your actual images.

### Recommendations

![Laptop recommendations](screenshots/recommendations.png)

### Extracted Requirements

![Extracted requirements](screenshots/extracted-requirements.png)

### No Exact Matches

![No exact matches](screenshots/no-match.png)

## Environment and Security

Create a `.env.example` file containing a placeholder only:

``` env
GEMINI_API_KEY=your_api_key_here
```

Ensure `.gitignore` includes:

``` gitignore
.env
.venv/
__pycache__/
*.py[cod]
```

Never commit API credentials.

## Current Limitations

-   Recommendations are limited to products in the local inventory.
-   Ranking scores are relative to the current filtered candidate set.
-   Numerical ranking currently supports the implemented weight and
    battery preferences.
-   When there are no exact matches, the application can report that
    result; intelligent fallback alternatives require additional
    implementation.
-   Live prices, availability, external reviews, and
    recommendation-quality evaluation are not currently part of the core
    pipeline.

## Future Improvements

-   Suggest alternatives when no exact matches are found.
-   Explain why each product was recommended.
-   Add current pricing, availability, and product reviews.
-   Support additional ranking criteria and use-case-specific
    suitability.
-   Evaluate recommendation quality against a defined test dataset.
-   Improve the interface with product cards and specification
    comparisons.

## Author

**Himanshu Bendale**

GitHub: [himanshuvb](https://github.com/himanshuvb)

------------------------------------------------------------------------

*SpecSense AI --- turning natural-language requirements into structured
product recommendations.*
