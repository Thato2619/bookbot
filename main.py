import sys
from stats import count_words
from stats import count_characters
from stats import sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    num_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)
    
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

main()

