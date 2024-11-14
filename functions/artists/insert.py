import tkinter as tk
import functions.artists.artists as art
from tkinter import messagebox




def toggle_insert_artists(root, cursor):
    for widget in root.winfo_children():
        widget.pack_forget()
        
    label = tk.Label(root, text="Insert into Artists form", font=('Arial', 16, 'bold'), bg='gray')
    label.pack(padx=50, pady=50)
    
    buttonframe = tk.Frame(root)
    

    artist_first_name_label = tk.Label(buttonframe, text="Artists's first name:")
    artist_first_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    artist_first_name_entry = tk.Entry(buttonframe)
    artist_first_name_entry.grid(row=1, column=1, padx=10, pady=10)

    artist_last_name_label = tk.Label(buttonframe, text="Artists's last name:")
    artist_last_name_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    artist_last_name_entry = tk.Entry(buttonframe) 
    artist_last_name_entry.grid(row=2, column=1, padx=10, pady=10)
    
    business_label = tk.Label(buttonframe, text="Business:")
    business_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    business_entry = tk.Entry(buttonframe) 
    business_entry.grid(row=3, column=1, padx=10, pady=10)
    
    yr_born_label = tk.Label(buttonframe, text="Year born:")
    yr_born_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")

    yr_born_entry = tk.Entry(buttonframe) 
    yr_born_entry.grid(row=4, column=1, padx=10, pady=10)

    submit_button = tk.Button(buttonframe, text="Submit", command=lambda: submit_insert_form(cursor, artist_first_name_entry, artist_last_name_entry, business_entry, yr_born_entry))
    submit_button.grid(row=5, column=1, padx=10, pady=20)
    
    buttonframe.pack()
    
    return_button = tk.Button(root, text="Return", command=lambda: art.toggle_artists(root, cursor))
    return_button.pack()
    
def submit_insert_form(cursor, artist_first_name_entry, artist_last_name_entry, business_entry, yr_born_entry):
    first_name = artist_first_name_entry.get()
    last_name = artist_last_name_entry.get()
    business = business_entry.get()
    yr_born = yr_born_entry.get()
    
    if not first_name or not last_name or not business or not yr_born:
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Form submitted successfully!\nArtist's first name: {first_name}\nArtist's last name:{last_name}\n"
                            f"Business: {business}\nYear born: {yr_born}")
        
    insert_database_artists(cursor, first_name, last_name, business, yr_born)
        
    
def insert_database_artists(cursor, first_name, last_name, business, yr_born):
    cursor.execute("""
        INSERT INTO artists(first_name, last_name, business, yr_born) 
        VALUES (?, ?, ?, ?)
    """, (first_name, last_name, business, yr_born))