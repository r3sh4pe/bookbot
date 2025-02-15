def main():
    book_content: str | None = None
    words: list[str] | None = None
    word_count: int | None = None

    with open("books/frankenstein.txt", "r") as f:
        book_content = f.read()

    words = book_content.split()
    word_count = len(words)

    print(word_count)


main()
