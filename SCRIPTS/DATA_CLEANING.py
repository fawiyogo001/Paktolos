# Basic Libraries
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import math
import datetime as dt
import calendar
from pathlib import Path
import glob 
import os

def COMBINE_INTERFACE(RAW_FILE_PATH, OUTPUT_FILE_PATH):

    try:
        os.remove(OUTPUT_FILE_PATH)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File not found.")

    RAW_PATH = Path(RAW_FILE_PATH)

    CSV_FILE_LIST = list(RAW_PATH.glob('*.csv'))
    COMBINED_DF = pd.concat([pd.read_csv(f) for f in CSV_FILE_LIST], ignore_index=True)

    COMBINED_DF.to_csv(OUTPUT_FILE_PATH, index=False)

    return COMBINED_DF

def LOAD_RAW_DATA(PATH):
    # Load the Raw CSV Data
    return pd.read_csv(PATH, parse_dates=["Date"])

def CLEAN_EXPENSE_DATA(df):

    # Column Validation
    EXPECTED_COLUMNS = ["Date", "Category", "Memo", "Income/Expenses", "Amount"]
    for col in EXPECTED_COLUMNS:
        if col not in df.columns:
            raise ValueError(f"Missing expected column: {col}")

    '''======================================================================================================='''


    '''
    Data Cleaning Part 1: Cleaning Memo Column
    --> Memo column contains 2 information: Item and Vendor along with the details of the Vendor Location. These columns are aimed to be separated for the purpose of data visualization.
    '''

    # Separate Memo Column into Item and Location Columns
    SPLIT_COLS = df["Memo"].str.split('@', n=1, expand=True)
    df["Item"] = SPLIT_COLS[0].str.strip()
    df["Location"] = SPLIT_COLS[1].str.strip().fillna("Blank")

    # Separate Location into 3 Columns: Vendor, Vendor Location, and District
    # df[["Item","Location"]] = df["Memo"].str.split('@', expand = True)

    # Count Numbers of Entities in the Location Column
    LOCATION_CHECK = []
    for i in df["Location"]: LOCATION_CHECK.append(str(i).count(",") + 1)
    df.insert(df.shape[1],"Location Check", LOCATION_CHECK, True)

    # Fill Empty Location With "Blank, Blank, Blank"
    df = df.fillna("Blank")
    df.loc[df["Location"] == "Blank", "Location"] = "Blank, Blank, Blank"

    # Fill Location Without Vendor Location with "Vendor, Blank, District" and Location without Vendor and Vendor Location with "Blank, Blank, District"
    LOCATION_FIXED=[]
    for i in df["Location"]:
        SPLIT_STR=i.split(',')
        if len(SPLIT_STR)==1:
            FINAL_STR="Blank, Blank, {FIRST_ELEMENT}".format(FIRST_ELEMENT=SPLIT_STR[0].strip())
            LOCATION_FIXED.append(FINAL_STR)
        elif len(SPLIT_STR)==2:
            FINAL_STR="{FIRST_ELEMENT}, Blank,{SECOND_ELEMENT}".format(FIRST_ELEMENT=SPLIT_STR[0].strip(), SECOND_ELEMENT=SPLIT_STR[1].strip())
            LOCATION_FIXED.append(FINAL_STR)
        else:
            LOCATION_FIXED.append(i.strip())

    df.insert(df.shape[1],"Location Fixed", LOCATION_FIXED, True)

    # Separate Location into 3 Columns: Vendor, Vendor Location, and District
    df[["Vendor","Vendor Location","District"]] = df["Location Fixed"].str.split(',', expand = True)

    # Drop Memo, Location, Location Check, and Location Fixed
    df = df.drop(columns=["Memo","Location","Location Check","Location Fixed"])

    # Remove Leading & Trailing Whitespaces 

    # Pre-Copy-on-Write Behaviour of Pandas (Pandas 3.0) is in Place
    # for i in (df[["Vendor","Vendor Location","District"]]):
    #     for j in range(0, len(df[i])):
    #         df[i].iloc[j] = df[i].iloc[j].strip()

    # Post-Copy-on-Write Behaviour of Pandas (Pandas 3.0) is in Place
    for col in (df[["Vendor","Vendor Location","District"]]): 
        df[col] = df[col].str.strip()

    '''======================================================================================================='''

    '''
    Data Cleaning Part 2: Item Column
    --> Item Column is arranged, so that the column does not contain blank values. If the a row happens to have "Blank" value on the Item column, the item column will take the value from the Category column.
    '''

    # Copy the Values from the Category if the Value in the Item Column is "Blank"
    df.loc[df["Item"]=="Blank","Item"] = df.loc[df["Item"]=="Blank","Category"]

    '''======================================================================================================='''

    '''
    Data Cleaning Part 3: Date Column
    --> The following information will be extracted from the Date column:
        1. The Name of the Day
        2. The Week Number (WW) 
        3. The Month Number (MM)
        4. The Year Number (YYYY)
    '''
    
    # Convert column to datetime if it isn't already
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    df = df[df["Date"].notna()]

    # Date Formatting on the "Date" Column and Generate "Day" and "Week" Columns Referring to Day of the Week and Week Number of the Year Respectively
    iso = df["Date"].dt.isocalendar()
    df["ISO Year"] = iso["year"]
    df["Year"] = df["Date"].dt.year
    df["Week"] = iso["week"]
    df["Day"] = df["Date"].dt.day_name()
    df["Month"] = df["Date"].dt.month
    df["Week Label"] = "W" + df["Week"].astype(str)

    # # Extract Month & Year from the Date
    MONTH_MAPPING = dict(enumerate(calendar.month_name))
    df['Month Label'] = df['Date'].dt.month.astype(int).replace(MONTH_MAPPING)
 
    # Remove Leading & Trailing Whitespaces 

    # Pre-Copy-on-Write Behaviour of Pandas (Pandas 3.0) is in Place
    # for i in (df[["Vendor","Vendor Location","District"]]):
    #     for j in range(0, len(df[i])):
    #         df[i].iloc[j] = df[i].iloc[j].strip()

    # Post-Copy-on-Write Behaviour of Pandas (Pandas 3.0) is in Place
    for col in (df[["Vendor","Vendor Location","District"]]):
        df[col] = df[col].str.strip()

    # Data Frame Rearrangement
    df = df[["Date","Year","ISO Year","Month","Month Label","Week","Week Label","Day","Category","Item","Vendor","Vendor Location","District","Income/Expenses","Amount"]]

    # Format to DD/MM/YYYY as a string (for display only)
    df["Formatted Date"] = df["Date"].dt.strftime('%d/%m/%Y')

    '''======================================================================================================='''

    '''
    Data Cleaning Part 4: Amount Column
    --> The Amount column is cleaned to have the positive values within the column.
    '''

    # Explicit Check for Numeric Conversion for Amount Column to Avoid String Type Issues
    df["Amount"] = pd.to_numeric(df["Amount"], errors='coerce').abs()

    # Make All the Values in Absolute Values
    df["Amount"] = df["Amount"].abs()

    '''======================================================================================================='''

    return df

def SAVE_PROCESSED_DATA(df, DATASET_FULL_CLEANED, EXPENSES_CLEANED, INCOME_CLEANED):
    # Save the Cleaned Dataframe to a CSV File
    df.to_csv(DATASET_FULL_CLEANED, index=False)
    df[(df["Income/Expenses"] == "Expenses")].to_csv(EXPENSES_CLEANED, index=False)
    df[(df["Income/Expenses"] == "Income")].to_csv(INCOME_CLEANED, index=False)

def DETECT_OUTLIERS_IQR_PER_CATEGORY(df, GROUP_COL, VALUE_COL, MULTIPLIER=1.5):

    '''
    GROUP_COL refers to the column containing the list of category names i.e. "Category"
    VALUE_COL refers to the column containing the list of values i.e. "Amount"
    '''

    df = df.copy()
    df["Outlier"] = False

    for CATEGORY in df[GROUP_COL].unique():
        SUBSET = df[df[GROUP_COL] == CATEGORY]
        Q1 = SUBSET[VALUE_COL].quantile(0.25)
        Q3 = SUBSET[VALUE_COL].quantile(0.75)
        IQR = Q3 - Q1
        LOWER_BOUND = Q1 - MULTIPLIER * IQR
        UPPER_BOUND = Q3 + MULTIPLIER * IQR

        # Flag as outlier or not
        OUTLIER_FLAGS = (SUBSET[VALUE_COL] < LOWER_BOUND) | (SUBSET[VALUE_COL] > UPPER_BOUND)

        df.loc[SUBSET.index, "Outlier"] = OUTLIER_FLAGS

    return df





'''================================================================================================================'''














'''====================================================UNUSED CODE=================================================='''


    # # Convert column names to lowercase and strip spaces
    # df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # # Remove duplicates
    # df.drop_duplicates(inplace=True)

    # # Remove unnecessary columns if any
    # columns_to_remove = ['Unnamed:_0'] if 'Unnamed:_0' in df.columns else []
    # df.drop(columns=columns_to_remove, inplace=True)

    # # Standardize date format
    # df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # # Old Way to Segregate Dates
    # DATE_FIXED = []
    # for date in df["Date"]:
    #     try:
    #         DATE_OBJECT = dt.datetime.strptime(str(date),'%Y-%m-%d')
    #         WEEK_NUMBER = DATE_OBJECT.isocalendar()[1]
    #         DATE_FIX = """{} W{} {}/{}/{}""".format(
    #             DATE_OBJECT.weekday(), 
    #             WEEK_NUMBER, 
    #             DATE_OBJECT.day, 
    #             DATE_OBJECT.month, 
    #             DATE_OBJECT.year
    #         )
    #         DATE_FIXED.append(DATE_FIX)
    #     except Exception as e:
    #         print(f"[ERROR] Skipping invalid date: {date} → {e}")
    #         DATE_FIXED.append("Invalid Date")
    #
    # df.insert(df.shape[1],"Date Fixed", DATE_FIXED, True)
    # df[["Day","Week","Date"]] = df["Date Fixed"].str.split(' ', expand = True)
       

    # Map the Day Column from Number of the Day to the Name of the Day 
    # DAY_MAPPING = dict(enumerate(calendar.day_name))
    # df['Day'] = df['Day'].astype(int).replace(DAY_MAPPING)

    
    # # Extract Month & Year from the Date
    # MONTH_MAPPING = dict(enumerate(calendar.month_name))
    # df['Year'], df['Month'] = df['Date'].dt.year, df['Date'].dt.month.astype(int).replace(MONTH_MAPPING)