def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def get_num_words(filepath):
    num_words = 0
    for i in get_book_text(filepath).split():
        num_words += 1
    return num_words


def get_char_count(filepath):
    char_dict = {}
    for i in get_book_text(filepath).lower():
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict


def sort_on(item):
    return item["num"]


# def sorted_dict(char_dict):
#     dict_list = []
#     for i in char_dict:
#         dict_list.append(i)
#     sorted_dict = dict_list.sort(reverse=True, key=sort_on)
#     return sorted_dict


def sorted_dict(char_dict):
    dict_list = []
    # 1. build the list of small dicts
    for char, count in char_dict.items():
        # make {"char": char, "num": count}
        # append it to dict_list
        if char.isalpha():
            dict_list.append({"char": char, "num": count})
        else:
            continue

    # 2. sort the list in place
    dict_list.sort(reverse=True, key=sort_on)

    # 3. return the sorted list
    return dict_list
