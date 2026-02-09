# SQLite to CSV Extractor

## 📖 Overview
This Python automation tool is for 
- connects to a remote SQLite database URL
- downloads the file into temporary memory
- detects all available tables
- exports them individually as CSV files 

It was designed to handle dynamic database structures where the table names might not be known beforehand.

## 🛠 Features
- **Remote Access:** Downloads database files directly from a URL.
- **Smart Memory Management:** Uses the `tempfile` library to process the database without permanently saving the `.db` file to your local disk.
- **Dynamic Introspection:** Automatically queries `sqlite_master` to find all table names, rather than hard-coding them.
- **Automated Export:** Loops through every table found and converts it to a clean CSV format.

## 📦 Libraries Used
- `sqlite3` (Database connection)
- `requests` (HTTP requests to download the file)
- `csv` (File formatting)
- `tempfile` (Temporary file creation)

## ⚙️ Logic & Methodology
1.  **Input Handling:** The script prompts the user for a URL. It includes logic to handle a default "test" URL if the user chooses to skip input.
2.  **Temporary Storage:** Instead of saving the binary database file to the project root, the script writes the content to a `NamedTemporaryFile`.
3.  This ensures the file is automatically deleted after the connection closes, keeping the workspace clean.
4.  **Data Extraction:** 
    - Connects to the SQLite database.
    - Selects all table names where type is 'table'.
    - Iterates through tables to fetch headers and rows.
    - Stores data in a dictionary structure: `{table_name: {'headers': [], 'data': []}}`.
    - Closes the connection to the database.
5.  **CSV Writing:** The script checks if data exists, then writes the headers and rows to the `./data/` directory using UTF-8 encoding.

## 🚀 How to Run

### Prerequisites
Make sure you have a folder named `data` in the same directory as the script, or the export will fail.
```bash
mkdir data
