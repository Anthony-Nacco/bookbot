from stats import count_words, count_characters, sort_chars

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    

def main():
    path = "books/frankenstein.txt"
    text = get_book_text("books/frankenstein.txt")
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    

    char_counts = count_characters(text)
    sorted_chars = sort_chars(char_counts)

    for entry in sorted_chars:
        if not entry["char"].isalpha():
            continue
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")    


main(
