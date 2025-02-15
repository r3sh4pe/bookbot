def count_characters(book_content: str) -> dict[str, int]:
    character_count: dict[str, int] = {}

    for character in book_content:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count


def main() -> None:
    book_content: str | None = None
    words: list[str] | None = None
    word_count: int | None = None
    char_count: dict[str, int] | None = None

    with open("books/frankenstein.txt", "r") as f:
        book_content = f.read()

    words = book_content.split()
    word_count = len(words)

    char_count = count_characters(book_content.lower())

    print(char_count)


main()
