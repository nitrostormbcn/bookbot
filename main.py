def main():
    path_to_file = "books/frankenstein.txt"

    contents = get_book(path_to_file)
    # print(contents)

    words = count_words(contents)
    # print(words)

    character_dict = count_characters(contents)
    # print(character_dict)

    report = format_report_string(path_to_file, words, character_dict)
    print(report)


def format_report_string(file: str, words: int, character_dict: dict):
    title = f"--- Begin report of {file} ---"
    word_report = f"{words} words found in the document"

    character_report = ""
    for character, char_count in character_dict.items():
        report_line = f"The '{character.replace("\n", "\\n")}' character was found {char_count} times\n"
        character_report += report_line

    report_end = "--- End report ---"
    report = title + "\n" + word_report + "\n" + "\n" + character_report + report_end
    return report


def get_book(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def count_words(text: str) -> int:
    count = len(text.split())
    return count


def count_characters(text: str) -> dict:
    seen_characters = {}
    for letter in text:
        # print(letter)
        lower_letter = letter.lower()
        if lower_letter not in seen_characters:
            seen_characters[lower_letter] = 1
        else:
            seen_characters[lower_letter] += 1
    return seen_characters


if __name__ == "__main__":
    main()
