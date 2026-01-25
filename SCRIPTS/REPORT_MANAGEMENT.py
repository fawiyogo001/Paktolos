# Libraries
import os
import json
import plotly.io as pio
from datetime import datetime
from pathlib import Path
from html2image import Html2Image
import pandas as pd
import tabulate
import sys

# Function
def REGISTER_REPORT_COMPONENT(REPORTING_TAG, TITLE, CONTENT, TYPE="text", HEADING="normal", BODY="normal", PATH=None, MANIFEST_PATH="FIGURE_MANIFEST.json"):

    try:
        NOTEBOOK_DIR = Path(os.getcwd()).resolve()
        PROJECT_ROOT = NOTEBOOK_DIR.parent

        MANIFEST_FILE = PROJECT_ROOT / MANIFEST_PATH

        ENTRY = {
            "reporting_tag": REPORTING_TAG,
            "title": TITLE,
            "type": TYPE,
            "heading": HEADING,
            "body": BODY,
            "content": CONTENT,
            "path": str(PATH).replace("\\", "/") if PATH else None
        }

        # Load existing manifest or start fresh
        if MANIFEST_FILE.exists():
            try:
                with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
                    MANIFEST = json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Manifest file is empty or corrupted. Reinitializing...")
                MANIFEST = []
        else:
            MANIFEST = []

        # Remove old entries with same path or title
        MANIFEST = [e for e in MANIFEST if e.get("reporting_tag") != REPORTING_TAG]

        # Add new entry
        MANIFEST.append(ENTRY)

        # Save updated manifest
        with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
            json.dump(MANIFEST, f, indent=2)

        if HEADING == "normal": 
            pass
        else: 
            print(f"✅ Registered component: {REPORTING_TAG} with Title {TITLE}")

    except Exception as e:
        print(f"❌ Error registering component: {e}")

def SAVE_PLOT_AND_REGISTER(FIG, FILENAME, TITLE, CAPTION, MANIFEST_PATH="FIGURE_MANIFEST.json"):
    
    try:
        NOTEBOOK_DIR = Path(os.getcwd()).resolve()
        PROJECT_ROOT = NOTEBOOK_DIR.parent

        PLOTS_FOLDER = PROJECT_ROOT / "ASSETS" / "PLOTS"
        # MANIFEST_FILE = PROJECT_ROOT / MANIFEST_PATH

        os.makedirs(PLOTS_FOLDER, exist_ok=True)

        FULL_PATH = PLOTS_FOLDER / FILENAME
        FULL_PATH_STR = str(FULL_PATH)

        ASSET_FOLDER = Path("ASSETS")
        DYNAMIC_REPORT_PLOT_PATH = ASSET_FOLDER / "PLOTS" / FILENAME

        # Save the image
        try:
            FIG.write_image(FULL_PATH_STR)
            print(f"✅ PNG saved with Dynamic Path: {DYNAMIC_REPORT_PLOT_PATH}")
        except Exception as e:
            print("⚠️ PNG export failed. Saving as HTML instead...")
            try:
                # Option 1 (safe fallback)
                HTML_PATH = FULL_PATH.with_suffix(".html")
                FIG.write_html(str(HTML_PATH))
                FULL_PATH_STR = str(HTML_PATH)
                print(f"✅ HTML saved: {FULL_PATH_STR}")

                # Convert HTML to PNG
                try:
                    hti = Html2Image(output_path=str(PLOTS_FOLDER))
                    hti.screenshot(
                        html_file=str(HTML_PATH),
                        save_as=HTML_PATH.replace(".html", ".png")
                    )
                    print(f"✅ PNG converted from HTML with Dynamic Path: {DYNAMIC_REPORT_PLOT_PATH}")
                except Exception as e:
                    print("⚠️ PNG conversion failed:", e)
            except:
                # Option 2 (manual HTML)
                HTML_STR = FIG.to_html(include_plotlyjs="cdn")
                HTML_PATH = FULL_PATH.replace(".png", ".html")
                with open(HTML_PATH, "w", encoding="utf-8") as f:
                    f.write(HTML_STR)
                print(f"✅ HTML saved manually at: {HTML_PATH}")    

        # Add new entry
        REGISTER_REPORT_COMPONENT(
            REPORTING_TAG=FILENAME,
            TITLE=TITLE,
            CONTENT=CAPTION,
            TYPE="figure",
            HEADING="h4",
            BODY="point",
            PATH=DYNAMIC_REPORT_PLOT_PATH,
            MANIFEST_PATH=MANIFEST_PATH
        )

    except Exception as err:
        print("❌ Unexpected failure during save/register:", err)

def LOAD_FIGURE_MANIFEST(FIGURE_MANIFEST_PATH):
    with open(str(FIGURE_MANIFEST_PATH), "r", encoding="utf-8") as f:
        FIGURE_MANIFEST = json.load(f)
    return FIGURE_MANIFEST

def GENERATE_REPORT(REPORT_PATH="REPORT.md", MANIFEST_PATH="FIGURE_MANIFEST.json"):

    NOTEBOOK_DIR = Path(os.getcwd()).resolve()
    PROJECT_ROOT = NOTEBOOK_DIR.parent

    REPORT_FILE = PROJECT_ROOT / REPORT_PATH
    MANIFEST_FILE = PROJECT_ROOT / MANIFEST_PATH

    os.makedirs(os.path.dirname(REPORT_PATH) or ".", exist_ok=True)

    FIGURE_MANIFEST = LOAD_FIGURE_MANIFEST(MANIFEST_FILE)

    with open(REPORT_FILE, "w") as f:
        f.write(f"# Data Analysis Report\n\n")
        f.write("Report generated on: {}\n\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        f.write("Because GitHub is unable to display Plotly interactive figures, a dynamic report is generated to compile each figure along with their respective captions.\n\n")
        f.write("For interactive features, please refer to the Jupyter notebooks in the 'NOTEBOOKS/' directory and rerun the cells to generate the plots.\n\n")

        f.write(f"<hr>\n\n")

        for ENTRY in FIGURE_MANIFEST:

            if ENTRY["heading"] == "normal":
                pass
            elif ENTRY["heading"] == "h4":
                f.write(f"#### {ENTRY['title']}\n\n")
            elif ENTRY["heading"] == "h3":
                f.write(f"### {ENTRY['title']}\n\n")
            elif ENTRY["heading"] == "h2":
                f.write(f"<hr>\n\n")
                f.write(f"## {ENTRY['title']}\n\n")

            if ENTRY["type"] == "figure":
                f.write(f"<p align='center'><img src='{ENTRY['path']}'></p>\n\n")
                f.write(f"*{ENTRY['content']}\n\n\n")
            elif ENTRY["type"] == "text":
                if ENTRY["body"] == "point":
                    f.write(f"* {ENTRY['content']}\n\n")
                elif ENTRY["body"] == "equation":
                    f.write(f"$$\n{ENTRY['content']}\n$$\n\n")
                elif ENTRY["body"] == "normal":
                    f.write(f"{ENTRY['content']}\n\n\n")
            elif ENTRY["type"] == "table":
                f.write(f"\n\n")
                f.write(f"<div align='center'>")
                f.write(f"\n\n")
                f.write(f"```markdown\n{ENTRY['content']}\n```")
                f.write(f"\n\n")
                f.write(f"</div>")
                f.write(f"\n\n")

        f.write("---\n\n")
        f.write("For more information, please refer to the Data Analysis Report Notebook [here](NOTEBOOKS/CASH_FLOW_DATA_ANALYSIS.ipynb) directory.\n")

    print(f"Report generated successfully at {REPORT_PATH}.")

def FORMAT_SUMMARY_TABLE(df):
    summary = {
        "Count": f"{int(df['Count'].iloc[0]):,}",
        "Mean": f"{df['Mean'].iloc[0]:.2f}",
        "Median": f"{df['Median'].iloc[0]:.2f}",
        "Standard Deviation": f"{df['Std Dev'].iloc[0]:.2f}",
        "Minimum": f"{df['Min'].iloc[0]:.2f}",
        "Lower Outlier Bound": f"{df['Lower Outlier Bound'].iloc[0]:.2f}",
        "Q1 (25%)": f"{df['Q1 (25%)'].iloc[0]:.2f}",
        "Q3 (75%)": f"{df['Q3 (75%)'].iloc[0]:.2f}",
        "Upper Outlier Bound": f"{df['Upper Outlier Bound'].iloc[0]:.2f}",
        "Maximum": f"{df['Max'].iloc[0]:.2f}",
        "IQR": f"{df['IQR'].iloc[0]:.2f}",
        "Skewness": f"{df['Skewness'].iloc[0]:.2f}",
        "Kurtosis": f"{df['Kurtosis'].iloc[0]:.2f}"
    }

    summary_df = pd.DataFrame(list(summary.items()), columns=["Metric", "Value"])
    return summary_df.to_markdown(index=False)

def FORMAT_VALUE(VALUE):
    if isinstance(VALUE, float):
        return f"{VALUE:.2f}"
    elif isinstance(VALUE, tuple):
        return f"({VALUE[0]:.2f}, {VALUE[1]:.2f})"
    else:
        return str(VALUE)