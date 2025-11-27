import sys
from stats import get_char_count, get_num_words, sorted_char_count


def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8-sig") as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    num_words = get_num_words(content)
    char_count = get_char_count(content)
    sorted_chars = sorted_char_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing the book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        character = entry["char"]
        if character.isalpha():
            print(f"{character}: {entry['num']}")
    print("============= END ===============")


main()
