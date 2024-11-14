from tkinter import messagebox

def list_books(cursor):
    cursor.execute("""SELECT * from books""")
    return cursor.fetchall()
    
    
def show_books(cursor):
    books = list_books(cursor)
    books_text = "\n".join([f"ID:{book[0]}  {book[1]} {book[2]} {book[3]} {book[4]} {book[5]}" for book in books])
    
    messagebox.showinfo("Books List", books_text)
    
