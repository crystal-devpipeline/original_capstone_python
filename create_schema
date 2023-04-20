import sqlite3

def create_schema():
    connection = sqlite3.connect("competency_tracker.db")
    cursor = connection.cursor()
    with open("competency_schema.sql") as infile:
        schema = infile.read()
        cursor.executescript(schema)
        connection.commit()


create_schema()