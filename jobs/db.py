from flask import g
import datetime
import sqlite3

PATH="db/jobs.sqlite"

def open_connection():
    connection = getattr(g, '_connection', None)
    if connection is None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit:
        results = connection.commit()
    else :
        results = cursor.fetchone() if single else cursor.fetchall()
    
    cursor.close()
    return results
