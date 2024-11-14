import tkinter as tk
from tkinter import messagebox
import sqlite3
import functions.books.books as bk



def toggle_search_books(root, cursor):
    for widget in root.winfo_children():
        widget.pack_forget()
        
    label = tk.Label(root, text="Search from Books form", font=('Arial', 16, 'bold'), bg='gray')
    label.pack(padx=50, pady=50)
    
    buttonframe = tk.Frame(root)
    
    search_label = tk.Label(buttonframe, text="Search ID:")
    search_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    search_entry = tk.Entry(buttonframe)
    search_entry.grid(row=0, column=1, padx=10, pady=10)
    
    submit_button = tk.Button(buttonframe, text="Submit", command=lambda: submit_search(cursor, search_entry))
    submit_button.grid(row=1, column=1, padx=10, pady=20)
    
    buttonframe.pack()
    
    return_button = tk.Button(root, text="Return", command=lambda: bk.toggle_books(root, cursor))
    return_button.pack()



def submit_search(cursor, search_entry):
    search = search_entry.get()
    if not search:
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Form submitted successfully!\nTrying to delete entry {search}")
        
    search_books(cursor, search)
    

def search_books(cursor, search):
    try:
        cursor.execute("SELECT * from books WHERE ID = ?", (search, ))
        messagebox.showinfo("Success", f"Record with an ID: {search} was successfully found or does not exist.\n")
        books = cursor.fetchall()
        books_text = "\n".join([f"ID:{book[0]}  {book[1]} {book[2]} {book[3]} {book[4]} {book[5]}" for book in books])
        messagebox.showinfo("Success", books_text)
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Tried to delete the record, {e}")
        