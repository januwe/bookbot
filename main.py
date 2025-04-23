#!/usr/bin/env python3

import sys
from stats import (
    get_num_words,
    get_chars_dict,
    chars_dict_to_sorted_list,
)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print_report(book_path, num_words, chars_sorted_list)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    try:
        with open(book_path) as f:
            pass
    except FileNotFoundError:
        print("The specified file does not exist.")
        sys.exit(1)

    main(book_path)
