from stats import get_num_words
import sys

def open_file_at_path(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_character_occurrences(contents):
    occurrence_map = {}
    for char in contents.lower():
        if char in occurrence_map:
            occurrence_map[char] += 1
        else:
            occurrence_map[char] = 1
    return occurrence_map

def dict_to_list(dict_from_list):
    list_from_dict = []
    for k in dict_from_list:
        v = dict_from_list[k]
        list_from_dict.append({"key": k, "value": v})
    return list_from_dict

def sort_on_value(list_of_dicts):
    return list_of_dicts["value"]

def print_char_report(list_of_char_occurrences):
    for occ in list_of_char_occurrences:
        print(f"{occ['key']}: {occ['value']}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = open_file_at_path(sys.argv[1])
    book_words_count = get_num_words(book)
    print(f"Found {book_words_count} total words.")
    book_character_occurrences = get_character_occurrences(book)

    chars_list = dict_to_list(book_character_occurrences)
    only_chars = []
    for char_occ in chars_list:
        if char_occ["key"].isalpha():
            only_chars.append(char_occ)

    only_chars.sort(reverse=True, key=sort_on_value)
    print_char_report(only_chars)

main()