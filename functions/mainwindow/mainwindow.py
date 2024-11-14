import tkinter as tk
import functions.books.books as bk
import functions.songs.songs as son
import functions.artists.artists as art
import functions.movies.movies as mov
import functions.saveas.saveAsCsv as CSV
import functions.saveas.saveAsJSON as JSON
import functions.saveas.saveAsTxt as TXT



def toggle_start(root, cursor): 
    for widget in root.winfo_children():
        widget.pack_forget()

    root.title("Main Window")

    books_button = tk.Button(root, text="Books", command=lambda: bk.toggle_books(root, cursor))
    movies_button = tk.Button(root, text="Movies", command=lambda: mov.toggle_movies(root, cursor))
    songs_button = tk.Button(root, text="Songs", command=lambda: son.toggle_songs(root, cursor))
    actors_button = tk.Button(root, text="Artists", command=lambda: art.toggle_artists(root, cursor))

    empty_space = tk.Frame(root, height=100, bg='gray').pack()

    welcome_label = tk.Label(root, text="Welcome to the database", font=('Arial', 20, 'bold'), bg='gray')
    welcome_label.pack()

    empty_space = tk.Frame(root, height=100, bg='gray').pack()

    choosing_label = tk.Label(root, text="Choose your table", font=('Arial', 16, 'bold'), bg='gray')
    choosing_label.pack()

    empty_space = tk.Frame(root, width=170, bg='gray').pack(side=tk.LEFT)
    books_button.pack(side=tk.LEFT, padx=25)
    movies_button.pack(side=tk.LEFT, padx=25)
    songs_button.pack(side=tk.LEFT, padx=25)
    actors_button.pack(side=tk.LEFT, padx=25)
    
    save_csv_button = tk.Button(root, text="Save as .csv", command=lambda: CSV.save_as_csv(root, cursor))
    save_csv_button.pack(pady=10)
    
    save_txt_button = tk.Button(root, text="Save as .txt", command=lambda: TXT.save_as_txt(root, cursor))
    save_txt_button.pack(pady=10)
    
    save_json_button = tk.Button(root, text="Save as .json", command=lambda: JSON.save_as_json(root, cursor))
    save_json_button.pack(pady=10)
    
    


