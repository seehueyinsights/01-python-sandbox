# 01-Python-Sandbox

**First Attempts - Dabbling in Python Scripts**

This repository contains my early attempts at Python coding. Each folder represents a different concept or tool I am learning.

## Table of Contents

### 1. [Unicode Reader Project](./unicode-project)
**Objective:** To read Unicode characters off a HTML Google Doc file and present results as readable text.
*   **Input:** URL Argument
*   **Method:** Uses Pandas to extract table data and map coordinates (x, y) to a visual grid.
*   **Result:** A rendered graphic from raw data.

### 2. [SQLite Extractor Project](./sqlite_extractor-project)
**Objective:** To access an external db via URL, download and extract the contents of the db into a local folder '\data'.
*   **Input:** URL Argument
*   **Method:** Uses `requests` and `tempfile` to process the database in memory, dynamically identifies tables using SQL introspection, and iterates through them.
*   **Result:** Individual CSV files for each table found in the database

### 3. [Tic-Tac-Toe Game](./tic_tac_toe)
**Objective:** To build an interactive, logic-based 2-player game that runs entirely in the command-line interface.
*   **Input:** User console input (integers 1-9) representing grid coordinates.
*   **Method:** Utilizes Python lists to manage board state, implements `while` loops for robust input validation, and employs algorithmic checks against pre-defined winning tuples (horizontal, vertical, and diagonal) to determine game status.
*   **Result:** A dynamic, text-based game session that updates the grid visual in real-time and automatically declares a winner or a draw.
---
