from tkinter import messagebox

def list_movies(cursor):
    cursor.execute("""SELECT * from movies""")
    return cursor.fetchall()
    
    
def show_movies(cursor):
    movies = list_movies(cursor)
    movies_text = "\n".join([f"ID:{movie[0]}  {movie[1]} {movie[2]} {movie[3]} {movie[4]} {movie[5]}" for movie in movies])
    
    messagebox.showinfo("movies List", movies_text)
    
