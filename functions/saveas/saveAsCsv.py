import tkinter as tk
import functions.mainwindow.mainwindow as mw
import csv
from tkinter import messagebox
    
    
    
def save_as_csv(root, cursor):
    
    for widget in root.winfo_children():
        widget.pack_forget()
        
    empty_space = tk.Frame(root, height=100, bg='gray').pack()
    
    select_label = tk.Label(root, text="Select table you would like to save as csv", font=('Arial', 20, 'bold'), bg='gray')
    select_label.pack()
    
    empty_space = tk.Frame(root, height=100, bg='gray').pack()
    
    books_button = tk.Button(root, text="Books", command=lambda: save_csv(cursor, "books"))
    movies_button = tk.Button(root, text="Movies", command=lambda: save_csv(cursor, "movies"))
    songs_button = tk.Button(root, text="Songs", command=lambda: save_csv(cursor, "songs"))
    actors_button = tk.Button(root, text="Artists", command=lambda: save_csv(cursor, "artists"))
    
    empty_space = tk.Frame(root, width=170, bg='gray').pack(side=tk.LEFT)

    books_button.pack(side=tk.LEFT, padx=25)
    movies_button.pack(side=tk.LEFT, padx=25)
    songs_button.pack(side=tk.LEFT, padx=25)
    actors_button.pack(side=tk.LEFT, padx=25)
    
    exit_button = tk.Button(root, text="Return", command=lambda: mw.toggle_start(root, cursor))
    exit_button.pack()


def save_csv(cursor, type):
    query = f"SELECT * FROM {type}"
    cursor.execute(query)
    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]

    with open(f"{type}.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(column_names)
        csv_writer.writerows(rows)
        
    messagebox.showinfo("Success", f"File was as saved as {type}.csv")
    
    

