# Libraries
import os
import json
import plotly.io as pio
from datetime import datetime
from pathlib import Path

# Function
def SAVE_PLOT_AND_REGISTER(FIG, FILENAME, TITLE, CAPTION, MANIFEST_PATH="FIGURE_MANIFEST.json"):
    
    try:
        NOTEBOOK_DIR = Path(os.getcwd()).resolve()
        PROJECT_ROOT = NOTEBOOK_DIR.parent

        PLOTS_FOLDER = PROJECT_ROOT / "ASSETS" / "PLOTS"
        MANIFEST_FILE = PROJECT_ROOT / MANIFEST_PATH

        os.makedirs(PLOTS_FOLDER, exist_ok=True)

        # FULL_PATH = os.path.join(FOLDER, FILENAME)
        FULL_PATH = PLOTS_FOLDER / FILENAME
        FULL_PATH_STR = str(FULL_PATH)

        # Save the image
        try:
            FIG.write_image(FULL_PATH_STR)
            print(f"✅ PNG saved: {FULL_PATH_STR}")
        except Exception as e:
            print("⚠️ PNG export failed. Saving as HTML instead...")
            try:
                # Option 1 (safe fallback)
                HTML_PATH = FULL_PATH.with_suffix(".html")
                FIG.write_html(str(HTML_PATH))
                FULL_PATH_STR = str(HTML_PATH)
                print(f"✅ HTML saved: {FULL_PATH_STR}")
            except:
                # Option 2 (manual HTML)
                HTML_STR = FIG.to_html(include_plotlyjs="cdn")
                HTML_PATH = FULL_PATH.replace(".png", ".html")
                with open(HTML_PATH, "w", encoding="utf-8") as f:
                    f.write(HTML_STR)
                print(f"✅ HTML saved manually at: {HTML_PATH}")    
            
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
        MANIFEST = [ENTRY for ENTRY in MANIFEST if ENTRY["path"] != FULL_PATH_STR and ENTRY["title"] != TITLE]

        # Add new entry
        MANIFEST.append({
            "title": TITLE,
            "path": FULL_PATH_STR.replace("\\", "/"),
            "caption": CAPTION
        })

        # Save updated manifest
        with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
            json.dump(MANIFEST, f, indent=2)

        print(f"✅ Saved and registered: {MANIFEST_FILE.name}")

    except Exception as err:
        print("❌ Unexpected failure during save/register:", err)

def LOAD_FIGURE_MANIFEST(FIGURE_MANIFEST_PATH):
    with open(FIGURE_MANIFEST_PATH, "r") as f:
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

        for FIGURE in FIGURE_MANIFEST:
            f.write(f"## {FIGURE['title']}\n\n")
            f.write(f"<p align='center'>\n  <img src='{FIGURE['path']}'>\n</p>\n\n")
            f.write(f"*{FIGURE['caption']}*\n\n\n")
        f.write("---\n\n")
        f.write("For more information, please refer to the Jupyter notebooks in the 'NOTEBOOKS/' directory.\n")

    print(f"Report generated successfully at {REPORT_FILE}.")

    