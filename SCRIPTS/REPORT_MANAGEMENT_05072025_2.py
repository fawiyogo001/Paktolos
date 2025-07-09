# Libraries
import os
import json
import plotly.io as pio
from datetime import datetime
from pathlib import Path

# Function
def REGISTER_REPORT_COMPONENT(TITLE, CONTENT, TYPE="text", PATH=None, MANIFEST_PATH="FIGURE_MANIFEST.json"):

    try:
        NOTEBOOK_DIR = Path(os.getcwd()).resolve()
        PROJECT_ROOT = NOTEBOOK_DIR.parent

        # REPORT_FILE = PROJECT_ROOT / REPORT_PATH
        MANIFEST_FILE = PROJECT_ROOT / MANIFEST_PATH

        # os.makedirs(os.path.dirname(REPORT_PATH) or ".", exist_ok=True)

        ENTRY = {
            "title": TITLE,
            "type": TYPE,
            "content": CONTENT,
            "path": PATH.replace("\\", "/") if PATH else None
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
        MANIFEST = [e for e in MANIFEST if e["title"] != TITLE]

        # Add new entry
        MANIFEST.append(ENTRY)

        # Save updated manifest
        with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
            json.dump(MANIFEST, f, indent=2)

        print(f"✅ Registered component: {TITLE}")

    except Exception as e:
        print(f"❌ Error registering component: {e}")

def SAVE_PLOT_AND_REGISTER(FIG, FILENAME, TITLE, CAPTION, MANIFEST_PATH="FIGURE_MANIFEST.json"):
    
    try:
        NOTEBOOK_DIR = Path(os.getcwd()).resolve()
        PROJECT_ROOT = NOTEBOOK_DIR.parent

        PLOTS_FOLDER = PROJECT_ROOT / "ASSETS" / "PLOTS"
        # MANIFEST_FILE = PROJECT_ROOT / MANIFEST_PATH

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

        # Add new entry
        REGISTER_REPORT_COMPONENT(
            TITLE=TITLE,
            CONTENT=CAPTION,
            TYPE="figure",
            PATH=FULL_PATH_STR,
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

        for ENTRY in FIGURE_MANIFEST:
            f.write(f"## {ENTRY['title']}\n\n")

            if ENTRY["type"] == "figure":
                f.write(f"<p align='center'><img src='{ENTRY['path']}' width='700'></p>\n\n")
                f.write(f"*{ENTRY['content']}\n\n\n")
            elif ENTRY["type"] == "text":
                f.write(f"{ENTRY['content']}\n\n")
            elif ENTRY["type"] == "table":
                f.write(f"```markdown\n{ENTRY['content']}\n```\n\n")

        f.write("---\n\n")
        f.write("For more information, please refer to the Jupyter notebooks in the 'NOTEBOOKS/' directory.\n")

    print(f"Report generated successfully at {REPORT_FILE}.")

    