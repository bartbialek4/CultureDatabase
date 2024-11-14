import tkinter as tk
import functions as func
import importlib
import pkgutil
import sqlite3
import atexit
import os

from functions.mainwindow import mainwindow


def cleanup(cursor, connection):
    cursor.close()
    connection.close()
    os.remove('database.db')
    print("Database file removed.")
    
def start_program():
    for loader, module_name, is_pkg in pkgutil.iter_modules(func.__path__):
        importlib.import_module(f"functions.{module_name}")
    
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("800x600")
    root.config(bg="gray")


    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE books(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT,
                    AUTHOR_FIRST_NAME TEXT,
                    AUTHOR_LAST_NAME TEXT,
                    GENRE TEXT,
                    YR_PUBLISHED INT
                    )""")

    cursor.execute("""CREATE TABLE movies(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT,
                    DIRECTOR_FIRST_NAME TEXT,
                    DIRECTOR_LAST_NAME TEXT,
                    GENRE TEXT,
                    YR_PUBLISHED INT 
                    )""")

    cursor.execute("""CREATE TABLE artists(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    FIRST_NAME TEXT,
                    LAST_NAME TEXT,
                    BUSINESS TEXT,
                    YR_BORN INT
                    )""")

    cursor.execute("""CREATE TABLE songs(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT,
                    AUTHOR_FIRST_NAME TEXT,
                    AUTHOR_LAST_NAME TEXT,
                    GENRE TEXT,
                    YR_PUBLISHED INT
                    )""")


    mainwindow.toggle_start(root, cursor)

    atexit.register(lambda: cleanup(cursor, connection))

    root.mainloop()
        

