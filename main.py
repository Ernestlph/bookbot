def main():
    book_path = "/home/ernest/workspace/github.com/Ernestlph/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    char_counts = get_num_char(text)
    for key,values in char_counts.items():
    
        print(f"The {key} character was found {values} times")
    print("--- End report ---")
    
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_char(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char.isalpha():
            char_counts.setdefault(char, 0)
            char_counts[char] += 1
    sorted_dict = sorted(char_counts.items(), key=lambda x:x[1], reverse=True)
    sorted_dict = dict(sorted_dict)
    return sorted_dict

main()