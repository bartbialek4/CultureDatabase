import tkinter as tk
import functions.artists.artists as art
from tkinter import messagebox
import sqlite3



def toggle_search_artists(root, cursor):
    for widget in root.winfo_children():
        widget.pack_forget()
        
    label = tk.Label(root, text="Search from Artists form", font=('Arial', 16, 'bold'), bg='gray')
    label.pack(padx=50, pady=50)
    
    buttonframe = tk.Frame(root)
    
    search_label = tk.Label(buttonframe, text="Search ID:")
    search_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    search_entry = tk.Entry(buttonframe)
    search_entry.grid(row=0, column=1, padx=10, pady=10)
    
    submit_button = tk.Button(buttonframe, text="Submit", command=lambda: submit_search(cursor, search_entry))
    submit_button.grid(row=1, column=1, padx=10, pady=20)
    
    buttonframe.pack()
    
    return_button = tk.Button(root, text="Return", command=lambda: art.toggle_artists(root, cursor))
    return_button.pack()



def submit_search(cursor, search_entry):
    search = search_entry.get()
    if not search:
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Form submitted successfully!\nTrying to delete entry {search}")
        
    search_artists(cursor, search)
    

def search_artists(cursor, search):
    try:
        cursor.execute("SELECT * from artists WHERE ID = ?", (search, ))
        messagebox.showinfo("Success", f"Record with an ID: {search} was successfully found or does not exist.\n")
        artists = cursor.fetchall()
        artists_text = "\n".join([f"ID:{artist[0]}  {artist[1]} {artist[2]} {artist[3]} {artist[4]}" for artist in artists])
        messagebox.showinfo("Success", artists_text)
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Tried to delete the record, {e}")