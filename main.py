def create_report(word_count: int, char_count: dict[str, int]) -> None:
    report_string: str = f"--- Begin report of books/frankenstein.txt ---\n{word_count} words found in the document\n\n"
    sorted_char_count = dict(sorted(char_count.items(), key=lambda c: c[1], reverse=True))

    for k, v in sorted_char_count.items():
        if k in "abcdefghijklmnopqrstuvwxyz":
            report_string += f"The '{k}' character was found {v} times\n"

    report_string += "--- End report ---"
    print(report_string)


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

    create_report(word_count, char_count)


main()
