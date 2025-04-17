def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    content = get_book_text(book_path)
    print(content)


main()