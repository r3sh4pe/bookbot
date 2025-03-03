from stats import get_num_words, count_characters, create_report


def main() -> None:
    book_content: str | None = None
    words: list[str] | None = None
    word_count: int | None = None
    char_count: dict[str, int] | None = None

    with open("books/frankenstein.txt", "r") as f:
        book_content = f.read()

    word_count = get_num_words(book_content)

    char_count = count_characters(book_content.lower())

    create_report(word_count, char_count)


main()
