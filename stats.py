def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    text = text.lower()
    char_counts = {}
    
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            
    return char_counts

def sort_characters(char_count_dict):
        """Takes a dictionary of characters and counts, returns sorted list of dictionaries."""
        sorted_list = []
        for char, num in char_count_dict.items():
            if char.isalpha():
                sorted_list.append({"char": char, "num":num})
        sorted_list.sort(reverse=True, key=lambda item: item["num"])
        return sorted_list