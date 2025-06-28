# <b>Paktolos — Personal Financial Flow Analytics</b>

<div style="text-align: justify">

<b>Paktolos</b> is a data analytics project focused on visualizing and understanding personal income and spending behavior from a time series and geospatial perspective.

Named after the mythological <b>Paktolos River</b>, into which King Midas washed away his golden touch, the project explores how wealth flows in and out of one’s life — just like the river rich with gold. It serves as a metaphor for the way financial habits shape prosperity (or the lack thereof) over time.

</div>

## Project Objective

<div style="text-align: justify"> 

To create a high-quality, professional-grade exploratory data analysis (EDA) and interactive dashboard to analyse:
- Spending patterns over time
- Behavioural spending habits (e.g. weekday vs weekend)
- Income vs expense dynamics (including surplus/deficit)
- Outlier detection and distribution skewness
- Seasonality, trend shifts, and change point detection
- Geospatial expense mapping by location (e.g. MRT stations & regions)
- Cumulative surplus and resource flow
- Statistical testing (e.g. Mann-Whitney U test) for behavioural insights

</div>

## Stack & Tools
<div style="text-align: justify"> 

- Programming Language: Python
- Libraries & Tools:
    - General:
        - Pandas
        - NumPy
        - typing
    - Data Visualisation:
        - Plotly 
        - Seaborn
        - Matplotlib
    - Statistical Analysis:
        - Scipy
        - Statsmodels
        - Ruptures
- IDE: 
    - Jupyter Notebooks (exploration, narrative, dashboard)
    - VSCode (code modularisation, data cleaning pipeline)

</div>

## Project Structure
paktolos/ <br>
│ <br>
├── data/ # Raw and cleaned CSVs <br>
├── scripts/ # Data cleaning, EDA, and visualization functions <br>
├── notebooks/ # Main analysis and visualization <br>
├── outputs/ # Exported visualizations (optional) <br>
├── README.md <br>
└── pyproject.toml <br>

## Highlights
<div style="text-align: justify"> 

- <b>Interactive trendlines</b> for monthly and weekly cash flow
- <b>Geospatial heatmap</b> of expenses by MRT district in Singapore
- <b>Statistical insight extraction</b> (outliers, skewness, kurtosis)
- <b>Change point detection</b> using `ruptures` for trend breaks
- <b>Data storytelling</b> with clean narratives and clear visual cues

</div>

## Data Dictionary
| Column            | Description                                                                                |
|-------------------|--------------------------------------------------------------------------------------------|
| `Date`            | Date of the transaction (format: YYYY-MM-DD)                                               |
| `Income/Expenses` | Transaction type: either `"Income"` or `"Expenses"`                                        |
| `Category`        | General category of the transaction (e.g., Food, Transport, Gift, etc.)                    |
| `Memo`            | Description of the item and/or location (e.g., "Top Up SIM Card")                          |
| `Amount`          | Amount in Singapore Dollars (S$); positive values for income & negative values for expenses|

## Setup Instructions

<div style="text-align: justify"> 

1. Clone the repository: <br>
git clone [https://github.com/fawiyogo001/paktolos.git](https://github.com/fawiyogo001/Paktolos) <br>
cd paktolos

2. Install poetry if not already installed: <br>
curl -sSL https://install.python-poetry.org | python3 -

3. Install dependencies: <br>
poetry install

4. Run Jupyter or scripts: <br>
poetry run jupyter notebook

</div>


## Future Improvements
<div style="text-align: justify"> 

- Time series forecasting (ARIMA, Prophet)
- Anomaly detection using ML
- Financial health scoring
- Budgeting assistant or alerts

</div>

<br>

<hr>
<p align="center"> End of Document</p>
<hr>