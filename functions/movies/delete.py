import tkinter as tk
import sqlite3
from tkinter import messagebox
import functions.movies.movies as mov


def toggle_delete_movies(root, cursor):
    for widget in root.winfo_children():
        widget.pack_forget()
    
    label = tk.Label(root, text="Delete from Movies form", font=('Arial', 16, 'bold'), bg='gray')
    label.pack(padx=50, pady=50)
    
    
    buttonframe = tk.Frame(root)
    
    delete_label = tk.Label(buttonframe, text="Delete ID:")
    delete_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    delete_entry = tk.Entry(buttonframe)
    delete_entry.grid(row=0, column=1, padx=10, pady=10)
    
    submit_button = tk.Button(buttonframe, text="Submit", command=lambda: submit_delete(cursor, delete_entry))
    submit_button.grid(row=1, column=1, padx=10, pady=20)
    
    buttonframe.pack()
    
    return_button = tk.Button(root, text="Return", command=lambda: mov.toggle_movies(root, cursor))
    return_button.pack()
    
    
def submit_delete(cursor, delete_entry):
        
    deleted = delete_entry.get()
    if not deleted:
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Form submitted successfully!\nTrying to delete entry {deleted}")
        
    delete_movies(cursor, deleted)
    
    
def delete_movies(cursor, deleted):
    try:
        cursor.execute("DELETE from movies WHERE ID = ?", (deleted, ))
        messagebox.showinfo("Success", f"Record with an ID: {deleted} was successfully deleted or does not exist.\n")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Tried to delete the record, {e}")