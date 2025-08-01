import sys
from stats import get_num_words, get_char_counts, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}..")
    
    book_text = get_book_text(book_path)
    
    num_words = get_num_words(book_text)
    char_counts = get_char_counts(book_text)
    sorted_chars = sort_characters(char_counts)
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
        
    print("============= END ===============")
    
main()
