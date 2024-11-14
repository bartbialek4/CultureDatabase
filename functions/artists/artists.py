import tkinter as tk
import functions.mainwindow.mainwindow as mw
import functions.artists.list as li
import functions.artists.delete as dele
import functions.artists.insert as ins 
import functions.artists.search as sear

def toggle_artists(root, cursor):
    
    for widget in root.winfo_children():
        widget.pack_forget()
        
    root.title("Artists")

    empty_space = tk.Frame(root, height=100, bg='gray').pack()

    artists_label = tk.Label(root, text="Artists table", font=('Arial', 20, 'bold'), bg='gray').pack()
    
    empty_space = tk.Frame(root, height=100, bg='gray').pack()

    artists_operations = tk.Label(root, text="Possible operations", font=('Arial', 16, 'bold'), bg='gray').pack()
    
    insert_button = tk.Button(root, text="Insert", command=lambda: ins.toggle_insert_artists(root, cursor))
    delete_button = tk.Button(root, text="Delete", command=lambda: dele.toggle_delete_artists(root, cursor))
    search_button = tk.Button(root, text="Search", command=lambda: sear.toggle_search_artists(root, cursor))
    list_button = tk.Button(root, text="List", command=lambda: li.show_artists(cursor))
    
    empty_space = tk.Frame(root, width=170, bg='gray').pack(side=tk.LEFT)
    insert_button.pack(side=tk.LEFT, padx=25)
    delete_button.pack(side=tk.LEFT, padx=25)
    search_button.pack(side=tk.LEFT, padx=25)
    list_button.pack(side=tk.LEFT, padx=25)
    
    empty_space = tk.Frame(root, height=50, bg='gray').pack()

    exit_button = tk.Button(root, text="Return", command=lambda: mw.toggle_start(root, cursor))
    exit_button.pack()
        

