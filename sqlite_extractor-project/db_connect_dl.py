# Connect to a database and learn about the tables and download all data

# Import the required library
import requests, tempfile
import sqlite3
import csv


# Function to obtain the database from a URL 
def get_file():

    default_url = "https://techassessment.blob.core.windows.net/aiap21-assessment-data/gas_monitoring.db"
    correct_url = "skip"
    
    while True:
    
        user_url = input(f"Enter the URL of the db:"'\n')
    
        if user_url == "":
            print(f"Invalid entry!")
            continue

        elif user_url == default_url: #check for valid entries
            print(f"Downloading sample db File!!!"'\n')
            break
            
        elif user_url == correct_url: #check for valid entries
            print(f"Skipped, using sample db File!!!"'\n')
            user_url = default_url
            break
    
    return user_url


# Function to connect to databse
def get_data(url):

    # Set the known local path of the database
    # db_name = "./data/gas_monitoring.db"  #path and db name for local storage

    try:
        # Download the file from url
        response = requests.get(url)
        response.raise_for_status()  # Check for errors like 404 Not Found.
        file_content = response.content

    # Create a managed temporary file.
    # The 'with' statement ensures it's automatically deleted afterward.
        with tempfile.NamedTemporaryFile(suffix=".db") as tmp_file:
        
            # Write the downloaded content into the temporary file.
            tmp_file.write(file_content)
            tmp_file.flush()    # Ensure data is written before connecting.
            print(f"Data stored temporarily at: {tmp_file.name}")
    
    
            # Use a dictionary to store data from all tables
            all_tables_data = {}

            # Setup the connection and cursor
            with sqlite3.connect(tmp_file.name) as db:
                c = db.cursor()
                print("Successfully Connected to SQLite")

                # Download the tables data and headers
                c.execute("SELECT name FROM sqlite_master WHERE type='table'")

                # Download the tables data 
                tables = [row[0] for row in c.fetchall()]
                print(f"Tables in the database: {tables}") #show tables names from db

                for name in tables:
                    # Skip SQLite's internal tables
                    if name.startswith('sqlite_'):
                        continue

                    sql_query = f'SELECT * FROM "{name}"' # this is the query statment
                    c.execute(sql_query,)  # tuples as safety

                    # Save data and heaadeers into variables
                    data = c.fetchall()
                    headers = [description[0] for description in c.description]
            
                    # Stores headers and data into dictionary, keyed by table name
                    all_tables_data[name] = {'headers': headers, 'data': data}

            # Close connection to db
            db.close()
            print("Successfully closed connection to SQLite")
            return all_tables_data

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
        # Return empty value if an error occurs
        return {}


#### MAIN ####

# Get the headers and the data by calling the functions
dataset = get_data(get_file())  # Option for user to enter url

# Alternatively, use this execution for a fixed url
# url = "https://techassessment.blob.core.windows.net/aiap21-assessment-data/gas_monitoring.db"
# dataset = get_data(url)

if dataset:
    for table_name, table_info in dataset.items(): # Unpack the data from dictionary in a loop
        headers = table_info['headers']  # data from dictionary key
        data = table_info['data']   # data from dictionary key
        
        # Check if any data exists before creating the csv file
        if not data:
            print(f"Skipping empty table: {table_name}")
            continue
        
        try:
            output_filename = f'./data/{table_name}.csv'  # Set the output filename and path

            # Open the file in 'write' mode with UTF-8 encoding
            # newline='' prevents extra blank rows from being written
            with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
            
                # Create a writer object
                writer = csv.writer(csvfile)

                # Write the header row first
                writer.writerow(headers)
            
                # Write the data rows
                writer.writerows(data)

                print(f"Data has been exported to {output_filename}")

        except IOError as e:
            print(f"Error writing to file: {e}")
else:
    print("No data was retrieved from the database. CSV file not created.")