import tkinter as tk
from tkinter import messagebox
import functions.songs.songs as son



def toggle_insert_songs(root, cursor):
    for widget in root.winfo_children():
        widget.pack_forget()
        
    label = tk.Label(root, text="Insert into songs form", font=('Arial', 16, 'bold'), bg='gray')
    label.pack(padx=50, pady=50)
    
    buttonframe = tk.Frame(root)
    
    
    name_label = tk.Label(buttonframe, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    name_entry = tk.Entry(buttonframe)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    author_first_name_label = tk.Label(buttonframe, text="Author's first name:")
    author_first_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    author_first_name_entry = tk.Entry(buttonframe)
    author_first_name_entry.grid(row=1, column=1, padx=10, pady=10)

    author_last_name_label = tk.Label(buttonframe, text="Author's last name:")
    author_last_name_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    author_last_name_entry = tk.Entry(buttonframe) 
    author_last_name_entry.grid(row=2, column=1, padx=10, pady=10)
    
    genre_label = tk.Label(buttonframe, text="Genre:")
    genre_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    genre_entry = tk.Entry(buttonframe) 
    genre_entry.grid(row=3, column=1, padx=10, pady=10)
    
    yr_published_label = tk.Label(buttonframe, text="Year published:")
    yr_published_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")

    yr_published_entry = tk.Entry(buttonframe) 
    yr_published_entry.grid(row=4, column=1, padx=10, pady=10)

    submit_button = tk.Button(buttonframe, text="Submit", command=lambda: submit_insert_form(cursor, name_entry, author_first_name_entry, author_last_name_entry, genre_entry, yr_published_entry))
    submit_button.grid(row=5, column=1, padx=10, pady=20)
    
    buttonframe.pack()
    
    return_button = tk.Button(root, text="Return", command=lambda: son.toggle_songs(root, cursor))
    return_button.pack()
    
    
def submit_insert_form(cursor, name_entry, author_first_name_entry, author_last_name_entry, genre_entry, yr_published_entry):
    name = name_entry.get()
    author_first_name = author_first_name_entry.get()
    author_last_name = author_last_name_entry.get()
    genre = genre_entry.get()
    yr_published = yr_published_entry.get()
    
    if not name or not author_first_name or not author_last_name or not genre or not yr_published:
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Form submitted successfully!\nName: {name}\nAuthor first name: {author_first_name}\nAuthor last name:{author_last_name}\n"
                            f"Genre: {genre}\nYear published: {yr_published}")
        
    insert_database_songs(cursor, name, author_first_name, author_last_name, genre, yr_published)
        
    
def insert_database_songs(cursor, name, author_first_name, author_last_name, genre, yr_published):
    cursor.execute("""
        INSERT INTO songs(NAME, AUTHOR_FIRST_NAME, AUTHOR_LAST_NAME, GENRE, YR_PUBLISHED) 
        VALUES (?, ?, ?, ?, ?)
    """, (name, author_first_name, author_last_name, genre, yr_published))