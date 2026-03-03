from validation import validate_isbn, validate_price
from operations import initialize_file, add_book, display_books, search_book

initialize_file()

while True:
    print("\n===== Book Store Management System =====")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book by Title")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        isbn = input("Enter ISBN (5 digits): ")
        if not validate_isbn(isbn):
            print("Invalid ISBN Format ❌")
            continue

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        price = input("Enter Price: ")

        if not validate_price(price):
            print("Invalid Price ❌")
            continue

        add_book(isbn, title, author, float(price))

    elif choice == "2":
        display_books()

    elif choice == "3":
        title = input("Enter Book Title to Search: ")
        search_book(title)

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice ❌")
