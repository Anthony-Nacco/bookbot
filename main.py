from stats import count_words, count_characters, sort_chars

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    char_counts = count_characters(text)
    sorted_chars = sort_chars(char_counts)

    print("--- Begin report of books/frankenstein.txt ---")
    for entry in sorted_chars:
        if not entry["char"].isalpha():
            continue
        print(f"The '{entry['char']}' character was found {entry['num']} times")
    print("--- End Report ---")    


main()
