# Folger: Exploratory Data Analysis for House Prices

This repository contains my step-by-step workflow EDA of the **King_County_House_prices_dataset.csv**. The main goal is to demostrate learned skills within the DS-ML Course @spicedAcademy. Also, to identify key factors influencing house prices and validate hypotheses.

## Project Structure

```
folger/                     # Project root
├─ data/                    # Raw data (ignored by Git via .gitignore)
│   └─ King_County_House_prices_dataset.csv
├─ notebooks/               # Jupyter Notebooks for each EDA stage
│   ├─ 1_Understanding_the_Data.ipynb
│   ├─ 2_Research_Questions_and_Hypothesis_Generation.ipynb
│   └─ 3_Exploring_the_Data.ipynb
├─ README.md                # Project overview (this file)
└─ requirements.txt         # Python dependencies
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



## Data

Place the file `King_County_House_prices_dataset.csv` into the `data/` folder. This folder is ignored by Git to prevent uploading large or sensitive files.

## Notebooks & Workflow

1. **Understanding the Data** (`1_Understanding_the_Data.ipynb`)
   - Load data and inspect structure
   - Check missing values and data types

2. **Research Questions & Hypotheses** (`2_Research_Questions_and_Hypothesis_Generation.ipynb`)
   - Formulate research questions
   - Derive measurable hypotheses and define indicators

3. **Exploring the Data** (`3_Exploring_the_Data.ipynb`)
   - Visualize distributions (histograms, bar charts)
   - Compute correlations and identify patterns
   - Clean data and perform feature engineering

## Usage

1. Open the project folder in **VS Code**.
2. Ensure the virtual environment is activated in the integrated terminal. Can also be launched in Jupyter Notebook (I used VS code):

   ```bash
   jupyter lab
   ```


## Next Steps

- Build predictive models (e.g., regression)
- Integrate external socio-economic data
- Deploy interactive dashboards or web app 

## Contributing

Feedback in any kind is welcome

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
