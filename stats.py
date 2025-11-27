def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    char_dict = {}
    for char in text.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def sort_on(items):
    return items["num"]


def sorted_char_count(char_counts):
    char_count_list = []
    for key in char_counts:
        char_count_list.append({"char": key, "num": char_counts[key]})
    
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list
    