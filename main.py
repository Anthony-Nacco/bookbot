from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    char_counts = count_characters(text)
    print(char_counts)

main()
