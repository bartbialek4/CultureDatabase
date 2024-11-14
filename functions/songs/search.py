import tkinter as tk
from tkinter import messagebox
import sqlite3
import functions.songs.songs as son



def toggle_search_songs(root, cursor):
    for widget in root.winfo_children():
        widget.pack_forget()
        
    label = tk.Label(root, text="Search from songs form", font=('Arial', 16, 'bold'), bg='gray')
    label.pack(padx=50, pady=50)
    
    buttonframe = tk.Frame(root)
    
    search_label = tk.Label(buttonframe, text="Search ID:")
    search_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    search_entry = tk.Entry(buttonframe)
    search_entry.grid(row=0, column=1, padx=10, pady=10)
    
    submit_button = tk.Button(buttonframe, text="Submit", command=lambda: submit_search(cursor, search_entry))
    submit_button.grid(row=1, column=1, padx=10, pady=20)
    
    buttonframe.pack()
    
    return_button = tk.Button(root, text="Return", command=lambda: son.toggle_songs(root, cursor))
    return_button.pack()



def submit_search(cursor, search_entry):
    search = search_entry.get()
    if not search:
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Form submitted successfully!\nTrying to delete entry {search}")
        
    search_songs(cursor, search)
    

def search_songs(cursor, search):
    try:
        cursor.execute("SELECT * from songs WHERE ID = ?", (search, ))
        messagebox.showinfo("Success", f"Record with an ID: {search} was successfully found or does not exist.\n")
        songs = cursor.fetchall()
        songs_text = "\n".join([f"ID:{song[0]}  {song[1]} {song[2]} {song[3]} {song[4]} {song[5]}" for song in songs])
        messagebox.showinfo("Success", songs_text)
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Tried to delete the record, {e}")
        