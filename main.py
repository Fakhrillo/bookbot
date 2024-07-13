def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_characters(text)
    get_report(text, num_words, num_characters)
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_characters(text):
    characters = {}
    for t in text:
        t_low = t.lower()
        if t_low in characters.keys():
            characters[t_low] += 1
        else:
            characters[t_low] = 0

    return characters

def get_report(text, num_words, num_characters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    sorted_items = sorted(num_characters.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_items:
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


main()
