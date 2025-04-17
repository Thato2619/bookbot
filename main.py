from stats import count_words
from stats import count_characters
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = count_words(text)
    print(f"{num_of_words} words found in the document")

    char_counts = count_characters(text)
    print(char_counts)

main()

