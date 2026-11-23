# Positron sample project

Small sample files for trying out each part of [Positron](https://positron.posit.co).

## Get started

1. In Positron, open the **New** menu in the Top Bar and select **New Folder from Git...**.
2. Enter `https://github.com/sharon-wang/positron-sample-project` as the Git repository URL and select **OK**. Positron clones the repo and opens the folder.
3. For Python, run **Python: Create Environment...** from the Command Palette. Choose **uv** (or **Venv**), pick a Python version and if prompted, check `requirements.txt` so the packages get installed.
4. For R, if htmltools is missing, run `install.packages("htmltools")` in an R console.

No Git? On GitHub, select **Code** > **Download ZIP**, unzip it, and drag the folder onto the Explorer in Positron (or use **Upload...** from the Explorer's right-click menu). Then open the folder with **File** > **Open Folder...**.

## Running the files

Open a `.py` or `.R` file and select the run button at the top right of the editor (or press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Enter</kbd>, <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>Enter</kbd> on Mac) to run the whole file in the Console.
`notebook.ipynb` opens in the Positron Notebook editor, where **Run All Cells** runs it.

## What each file is for

| File | Opens or fills |
|---|---|
| `data-frames.py`, `data-frames.R` | Console, Variables pane, Data Explorer (`weather`), Object Explorer (`project`) |
| `plots.py`, `plots.R` | Plots pane, with three plots in the history filmstrip |
| `viewer.R` | Viewer pane |
| `cells.py`, `cells.R` | Code cells (`# %%`) with Run Cell, Run Next and Run Above |
| `notebook.ipynb` | Positron Notebook editor |
| `app.py` | Run App button (Streamlit) |
| `connections.py` | Data Connections, a connection from the Python session (needs Positron `2026.12` or later) |
| `data/weather.csv` | Import Data dialog |
| `data/nested.json` | Object Explorer from a JSON file |
| `data/weather.sqlite` | Data Connections (SQLite) |
| `data/weather.dta` | Data Explorer, Stata file (needs Positron `2026.12` or later) |

The files in `data/` are made by `scripts/make_data.py`.
To remake them, run `python scripts/make_data.py` from this folder with the project's environment active (it needs `pandas` for `weather.dta`).
