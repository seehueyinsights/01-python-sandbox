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

---
