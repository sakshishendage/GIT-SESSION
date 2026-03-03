import pandas as pd
import os
file_name = "books.csv"
def initialize_file():
    if not os.path.exists(file_name):
        df = pd.DataFrame(columns=["ISBN", "Title", "Author", "Price"])
        df.to_csv(file_name, index=False)
def add_book(isbn, title, author, price):
    df = pd.read_csv(file_name)
    new_book = {
        "ISBN": isbn,
        "Title": title,
        "Author": author,
        "Price": price
    }
    df = pd.concat([df, pd.DataFrame([new_book])], ignore_index=True)
    df.to_csv(file_name, index=False)
    print("Book Added Successfully ✅")
def display_books():
    df = pd.read_csv(file_name)
    if df.empty:
        print("No Books Found")
    else:
        print("\n📚 Book List:")
        print(df)
def search_book(title):
    df = pd.read_csv(file_name)
    result = df[df["Title"].str.lower() == title.lower()]
    if not result.empty:
        print("\n🔍 Book Found:")
        print(result)
    else:
        print("Book Not Found ❌")
