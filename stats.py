def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

    def sort_on(chars):
        return chars[char]
    