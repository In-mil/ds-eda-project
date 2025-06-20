
# 🏘️ King County House Prices – EDA Project

*An EDA project for the **Data Science / Machine Learning Bootcamp @ Spiced Academy***  
Author: **Folger In‑mil** · IDE: **VS Code** · Python 3.11

---

## Project Goal  

> **Analyse data set and provide for an example customer at least 3 options** 

We start with **exploratory data analysis (EDA)** on the public *King_County_House_prices_dataset.csv*
and finish with  recommendations for one exemplar client.

---

## Repository Structure

```text
├─ data/                          
│   └─ 20250618_King_county_house_sales_ks_JOIN.csv
│   └─ df1_understanding_the_data.csv
│   └─ eda.csv
│
├─ notebooks/                     # Step‑by‑step EDA in Jupyter
│   ├─ 1_Understanding_the_Data.ipynb
│   ├─ 2_Research_Questions_and_Hypothesis_Generation.ipynb
│   ├─ 3_Exploring_the_Data.ipynb
│   └─ 4_Customer_assignment_NJ.ipynb
│
├─ reports/                       # Exported PDF slides & dashboard snapshots
│   └─ 20250619_offer_overview_NJ.pdf
│   └─ 20250619_offer_overview_NJ.xlsx
│   └─ EDA_Miro_board.pdf
│   └─ options_for_customer.csv
│   └─ figures/
│       └─ 0001_tbb
│       └─ 0002_tbb
│       └─ 0003_tbb
│       └─ 0004_tbb
├─ scripts/                      
│   ├─ 1_Understanding_the_Data.py
│   ├─ 3_Exploring_the_Data.py
│   └─ 4_Customer_assignment_NJ.py
├─ requirements.txt
└─ README.md                      # ← you are here
```



## Prerequisites

- Python 3.8+ installed
- VS Code with the **Python** and **Jupyter** extensions installed

## Installation

1. **Clone the repository**

   ```bash
   git clone git@github.com:In-mil/ds-eda-project.git
   cd Documents/spicedAcademy/ds-eda[...]
   ```

2. **Create a virtual environment**

   ```bash
   pyenv local 3.11.3
   python -m venv .venv #credentials copy&pasted from sql course
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt #install dependencies
   ```


## Notebook Guide & Key Findings

| Notebook | Purpose | Highlight |
|----------|---------|-----------|
| **1 Understanding the Data** | Load CSV · dtype audit · missing‑value heat‑map | Only 3 columns needed imputation (`yr_renovated`, `sqft_basement`, `view`). |
| **2 Research Questions** | Formulate research questions & hypotheses | Five measurable hypotheses (condition, renovation, age, popularity, socio‑economics). |
| **3 Exploring the Data** | Distributions · correlations · outlier curation | `sqft_living` & `grade` strongest positive price drivers (ρ ≈ 0.7). |
| **4 Customer Assignment – Nicole J.** | Persona‑driven filtering & KPI dashboard | 8 central ZIP codes found with median price ≈700‑900 k USD and high walk‑scores. |

*(PDF summaries live in `reports/`.)*

---

## Data Dictionary  <sup>(core 21 columns)</sup>

| Column | Description |
|--------|-------------|
| `id` | Unique listing identifier |
| `date` | Sale date *(converted to `datetime`)* |
| `price` | Target – sale price (USD) |
| `bedrooms`, `bathrooms` | Room counts |
| `sqft_living`, `sqft_lot` | Interior / lot size in ft² |
| `floors` | Number of levels |
| `waterfront`, `view` | Binary/ordinal view flags |
| `condition`, `grade` | Overall quality scores |
| `sqft_above`, `sqft_basement` | Split of living area |
| `yr_built`, `yr_renovated` | Construction / renovation year *(converted to 'int')* |
| `zipcode`, `lat`, `long` | Location |
| `sqft_living15`, `sqft_lot15` | Neighbourhood (15 nearest) averages |


---

## Client Personas & Deliverables

| Persona | Needs | Deliverable |
|---------|-------|------------|
| **Nicole Johnson** *(buyer)* | Lively, central neighbourhood • mid‑range budget • move within ≤12 mo | dashboard overview + shortlist CSV |

---

## License & Credits

- Data: © Kaggle (King County House Sales) – CC0 Public Domain  
- Code & visualisations: MIT License (see `LICENSE`)  
models are wrong, but some are useful.” – George Box*

---

V.1.0 as of 18 Jun 2025
