def count_words(text):
    return len(text.split())

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_chars(char_counts):
    sorted_list = [{"char": char, "num": count} for char, count in char_counts.items()]

    def get_num(d):
        return d["num"]
    
    sorted_list.sort(key=get_num, reverse=True)
    return sorted_list
    
