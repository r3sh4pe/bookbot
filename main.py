def main():
    book_content: str | None = None

    with open("books/frankenstein.txt", "r") as f:
        book_content = f.read()

    print(book_content)


main()
