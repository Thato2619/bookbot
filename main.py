def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = count_words(text)
    print(f"{num_of_words} words found in the document")

main()

