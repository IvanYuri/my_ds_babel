import pandas as pd
import csv
import sqlite3

def sql_to_csv():

    # Connect to the SQLite database
    conn = sqlite3.connect('all_fault_line.db')
    
    # Get cursor
    cursor = conn.cursor()
    
    # Execute query to get all data from the specified table
    cursor.execute("SELECT * FROM fault_lines")
    
    # Fetch all rows
    rows = cursor.fetchall()
    
    # Get column names
    headers = [description[0] for description in cursor.description]

    # Prepare CSV data
    csv_data = ','.join(headers) + '\n'  # Header row
    for row in rows:
        csv_data += ','.join(map(str, row)) + '\n'

    with open('all_fault_lines.csv', 'w', encoding='utf=8') as csv_file:
        csv_file.write(csv_data)

    conn.close()

# Part II, convert CSV to SQL

def csv_to_sql():
    # this line creates the db file if not exist
    conn = sqlite3.connect('list_volcano.db')

    # this line opens the csv using pandas
    df = pd.read_csv('list_volcano.csv')

    # this line converts csv to database(db)
    df.to_sql('Volcanos', conn, if_exists='replace', index=False)

    # create a cursor object to manipulate the data
    cur = conn.cursor()

    # fetch and display data for testing purposes
    for row in cur.execute('SELECT * FROM Volcanos'):
        print(row)
        
    # close connection
    conn.close()

# sql_to_csv()
sql_to_csv()

# call the function
csv_to_sql()


