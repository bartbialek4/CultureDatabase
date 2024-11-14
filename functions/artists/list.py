from tkinter import messagebox

def list_artists(cursor):
    cursor.execute("""SELECT * from artists""")
    return cursor.fetchall()
    
    
def show_artists(cursor):
    artists = list_artists(cursor)
    artists_text = "\n".join([f"ID:{artist[0]}  {artist[1]} {artist[2]} {artist[3]} {artist[4]}" for artist in artists])
    
    messagebox.showinfo("Artists List", artists_text)
    
