import sqlite3

CONN=CONN = sqlite3.connect('CustomerTable.db')
CUR = CONN.cursor()

CONN.execute("""CREATE TABLE CustomersTable (
    id INTEGER PRIMARY KEY,
    first_name STRING,
    last_name  STRING
    );
            """)