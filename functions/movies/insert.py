import tkinter as tk
from tkinter import messagebox
import functions.movies.movies as mov



def toggle_insert_movies(root, cursor):
    for widget in root.winfo_children():
        widget.pack_forget()
        
    label = tk.Label(root, text="Insert into Movies form", font=('Arial', 16, 'bold'), bg='gray')
    label.pack(padx=50, pady=50)
    
    buttonframe = tk.Frame(root)
    
    
    name_label = tk.Label(buttonframe, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    name_entry = tk.Entry(buttonframe)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    director_first_name_label = tk.Label(buttonframe, text="Director's first name:")
    director_first_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    director_first_name_entry = tk.Entry(buttonframe)
    director_first_name_entry.grid(row=1, column=1, padx=10, pady=10)

    director_last_name_label = tk.Label(buttonframe, text="Director's last name:")
    director_last_name_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    director_last_name_entry = tk.Entry(buttonframe) 
    director_last_name_entry.grid(row=2, column=1, padx=10, pady=10)
    
    genre_label = tk.Label(buttonframe, text="Genre:")
    genre_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    genre_entry = tk.Entry(buttonframe) 
    genre_entry.grid(row=3, column=1, padx=10, pady=10)
    
    yr_published_label = tk.Label(buttonframe, text="Year published:")
    yr_published_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")

    yr_published_entry = tk.Entry(buttonframe) 
    yr_published_entry.grid(row=4, column=1, padx=10, pady=10)

    submit_button = tk.Button(buttonframe, text="Submit", command=lambda: submit_insert_form(cursor, name_entry, director_first_name_entry, director_last_name_entry, genre_entry, yr_published_entry))
    submit_button.grid(row=5, column=1, padx=10, pady=20)
    
    buttonframe.pack()
    
    return_button = tk.Button(root, text="Return", command=lambda: mov.toggle_movies(root, cursor))
    return_button.pack()
    
    
def submit_insert_form(cursor, name_entry, director_first_name_entry, director_last_name_entry, genre_entry, yr_published_entry):
    name = name_entry.get()
    director_first_name = director_first_name_entry.get()
    director_last_name = director_last_name_entry.get()
    genre = genre_entry.get()
    yr_published = yr_published_entry.get()
    
    if not name or not director_first_name or not director_last_name or not genre or not yr_published:
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Form submitted successfully!\nName: {name}\nDirector's first name: {director_first_name}\nDirectorn's last name:{director_last_name}\n"
                            f"Genre: {genre}\nYear published: {yr_published}")
        
    insert_database_movies(cursor, name, director_first_name, director_last_name, genre, yr_published)
        
    
def insert_database_movies(cursor, name, director_first_name, director_last_name, genre, yr_published):
    cursor.execute("""
        INSERT INTO movies(NAME, director_first_name, director_last_name, GENRE, YR_PUBLISHED) 
        VALUES (?, ?, ?, ?, ?)
    """, (name, director_first_name, director_last_name, genre, yr_published))