import sqlite3

def process_data(records):
    """
    BUG: This function opens a new database connection for every single record.
    Under load, this will exhaust the connection pool and crash.
    """
    for record in records:
        # Opening connection inside the loop (BAD)
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        # We create the table first just so the code doesn't crash on the first run
        cursor.execute("CREATE TABLE IF NOT EXISTS transactions (id INTEGER, amount REAL)")
        cursor.execute("INSERT INTO transactions (id, amount) VALUES (?, ?)", record)
        conn.commit()
        conn.close()