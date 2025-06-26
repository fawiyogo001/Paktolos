# Basic Libraries
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, mannwhitneyu, ttest_ind, sem, t
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Literal, Tuple


def DESCRIBE_VARIABLE(df, VALUE_COL, EXCLUDE_OUTLIERS, SHOW_PLOT=True):
    df = df.copy()
    DATA = df[VALUE_COL].dropna()

    # Outlier filtering using IQR
    if EXCLUDE_OUTLIERS:
        Q1 = DATA.quantile(0.25)
        Q3 = DATA.quantile(0.75)
        IQR = Q3 - Q1
        LOWER_BOUND = Q1 - 1.5 * IQR
        UPPER_BOUND = Q3 + 1.5 * IQR
        DATA = DATA[(DATA >= LOWER_BOUND) & (DATA <= UPPER_BOUND)]
    else:
        Q1 = DATA.quantile(0.25)
        Q3 = DATA.quantile(0.75)
        IQR = Q3 - Q1
        LOWER_BOUND = Q1 - 1.5 * IQR
        UPPER_BOUND = Q3 + 1.5 * IQR

    # Descriptive Statistics
    SUMMARY = {
        "Count": len(DATA),
        "Mean": round(DATA.mean(),2),
        "Median": DATA.median(),
        "Std Dev": round(DATA.std(),2),
        "Min": DATA.min(),
        "Lower Outlier Bound":LOWER_BOUND,
        "Q1 (25%)": Q1,
        "Q3 (75%)": Q3,
        "Upper Outlier Bound":UPPER_BOUND,
        "IQR": IQR,
        "Max": DATA.max(),
        "Skewness": round(skew(DATA),2),
        "Kurtosis": round(kurtosis(DATA),2)
    }

    SUMMARY_DF = pd.DataFrame(SUMMARY, index=[VALUE_COL])

    return SUMMARY_DF

def DAY_TYPE_LABELLING(df, DAY_OF_WEEK_COL, WEEKEND_LIST):
    if DAY_OF_WEEK_COL not in df.columns:
        raise ValueError(f"Column '{DAY_OF_WEEK_COL}' does not exist in the DataFrame.")
    
    if df[DAY_OF_WEEK_COL].isnull().any():
        raise ValueError(f"Column '{DAY_OF_WEEK_COL}' contains null values.")
    
    df["Day Type"] = df[DAY_OF_WEEK_COL].apply(lambda x: "Weekend" if x in WEEKEND_LIST else "Weekday")
    
    return df

def TEMPORAL_AGGREGATION(df, TIME_INTERVAL_COL, AMOUNT_COL):
    df = df.groupby([TIME_INTERVAL_COL]).agg(
        TOTAL_AMOUNT=(AMOUNT_COL, "sum"),
        TRANSACTION_FREQUENCY=(AMOUNT_COL, "count")
    ).reset_index()

    df["AVERAGE_AMOUNT"] = (round(df["TOTAL_AMOUNT"] / df["TRANSACTION_FREQUENCY"], 2))

    return df

def RUN_STAT_TEST(
    GROUP1,  # e.g., weekday data (Series or array)
    GROUP2,  # e.g., weekend data
    METHOD: Literal["mannwhitney", "ttest"] = "mannwhitney",
    DIRECTION: Literal["two-sided", "greater", "less"] = "two-sided",
    CONFIDENCE: float = 0.95
) -> dict:
    """
    Run a statistical test with confidence intervals between two groups.
    
    Parameters:
        group1: First dataset (e.g., weekday spending)
        group2: Second dataset (e.g., weekend spending)
        method: Statistical test ("mannwhitney" or "ttest")
        direction: Hypothesis direction ("two-sided", "greater", or "less")
        confidence: Confidence level (e.g. 0.95 for 95%)

    Returns:
        A dictionary containing:
            - Test name
            - p-value
            - Mean + confidence interval for both groups
            - Conclusion based on significance
    """

    # Convert to arrays and drop missing
    GROUP1 = np.array(GROUP1.dropna())
    GROUP2 = np.array(GROUP2.dropna())

    RESULT = {}

    # Perform statistical test
    if METHOD == "mannwhitney":
        STAT, P_VALUE = mannwhitneyu(GROUP1, GROUP2, alternative=DIRECTION)
        RESULT["Test"] = "Mann-Whitney U Test"
    elif METHOD == "ttest":
        STAT, P_VALUE = ttest_ind(GROUP1, GROUP2, equal_var=False, alternative=DIRECTION)
        RESULT["Test"] = "Two-sample t-test"
    else:
        raise ValueError("Choose 'mannwhitney' or 'ttest'.")

    # Function for Confidence Interval
    def MEAN_CI(DATA: np.ndarray) -> Tuple[float, float, float]:
        '''
        mean - t(alpha/2) * std / sqrt(n) < mean < mean + t(alpha/2) * std / sqrt(n)
        '''

        n = len(DATA)
        MEAN = np.mean(DATA)

        # Right-Tailed Test -> 1 + Confidence Level 
        MARGIN_OF_ERROR = sem(DATA) * t.ppf((1 + CONFIDENCE) / 2., n - 1)
        return MEAN, MEAN - MARGIN_OF_ERROR, MEAN + MARGIN_OF_ERROR

    # Compute means and CIs
    G1_MEAN, G1_LOW, G1_HIGH = MEAN_CI(GROUP1)
    G2_MEAN, G2_LOW, G2_HIGH = MEAN_CI(GROUP2)

    RESULT.update({
        "p-value": round(P_VALUE, 6),
        "Group1_Mean": round(G1_MEAN, 2),
        "Group1_CI": (round(G1_LOW, 2), round(G1_HIGH, 2)),
        "Group2_Mean": round(G2_MEAN, 2),
        "Group2_CI": (round(G2_LOW, 2), round(G2_HIGH, 2)),
        "Conclusion": "Reject H₀ (Significant)" if P_VALUE < (1 - CONFIDENCE)
                      else "Fail to Reject H₀ (Not Significant)"
    })

    return RESULT


def MAP_STATION_COORDINATES(df, DISTRICT_COL: str, COORDS_PATH: str):
    """
    Join MRT coordinates to transaction dataframe based on MRT station name (District).
    
    Parameters:
    - df: Main DataFrame
    - district_col: Column in df that contains MRT station names (e.g., 'District')
    - coords_path: Path to CSV file with MRT station coordinates
    
    Returns:
    - DataFrame with added 'Latitude' and 'Longitude' columns
    - Also prints % of stations matched
    """
    COORDS_DF = pd.read_csv(COORDS_PATH)
    
    # Standardize casing/whitespace
    df[DISTRICT_COL] = df[DISTRICT_COL].str.strip().str.title()
    COORDS_DF["Station"] = COORDS_DF["Station"].str.strip().str.title()

    # Merge
    MERGED_DF = df.merge(
        COORDS_DF, 
        how="left",
        left_on=DISTRICT_COL, 
        right_on="Station"
    )

    # Report matching stats
    TOTAL_RECORDS = len(df)
    MATCHED_RECORDS = MERGED_DF["Latitude"].notna().sum()
    print(f"✅ Matched {MATCHED_RECORDS} out of {TOTAL_RECORDS} records ({MATCHED_RECORDS/TOTAL_RECORDS:.1%})")

    # Optional: flag missing values
    MERGED_DF["Coordinates Available"] = MERGED_DF["Latitude"].notna()

    return MERGED_DF
