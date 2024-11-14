from tkinter import messagebox

def list_songs(cursor):
    cursor.execute("""SELECT * from songs""")
    return cursor.fetchall()
    
    
def show_songs(cursor):
    songs = list_songs(cursor)
    songs_text = "\n".join([f"ID:{song[0]}  {song[1]} {song[2]} {song[3]} {song[4]} {song[5]}" for song in songs])
    
    messagebox.showinfo("Songs List", songs_text)
    
