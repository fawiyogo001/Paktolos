# Libraries
import os
import json
import plotly.io as pio
from datetime import datetime
from pathlib import Path

MANIFEST_PATH="FIGURE_MANIFEST.json"
NOTEBOOK_DIR = Path(os.getcwd()).resolve()
PROJECT_ROOT = NOTEBOOK_DIR.parent

# REPORT_FILE = PROJECT_ROOT / REPORT_PATH
MANIFEST_FILE = PROJECT_ROOT / MANIFEST_PATH

if MANIFEST_FILE.exists():
    print("File exists!")
else:
    print("File does not exist!")












# folder = "ASSETS/PLOTS"
# filename = "test_output.txt"
# full_path = os.path.join(folder, filename)

# os.makedirs(folder, exist_ok=True)

# with open(full_path, "w", encoding="utf-8") as f:
#     f.write("✅ File successfully written!")

# print(f"Written to: {full_path}")
# print("File exists?", os.path.exists(full_path))
# print(full_path)