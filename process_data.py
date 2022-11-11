def to_dictionary(d_type, name, value):
    """receives parameters and returns a dictionary with them"""
    current_dict = {
        'd_type': d_type,
        'elements': {
            'name': name,
            'value': value
        }
    }
    return current_dict


def format_elements(dicto):
    """function that receives a dictionary and formats its elements"""
    formatted_list = f"{dicto['elements']['name']} {dicto['elements']['value']}"
    return formatted_list


def parse_dictionary(dictionaries):
    """
    function that receives a list of dictionaries
    converts them into a processable form
    returns a list of the elements
    """
    texts = []
    ids = []
    numeric = []
    for dictionary in dictionaries:
        if dictionary["d_type"] == 'VAL':
            chosen_list = numeric
        elif dictionary["d_type"] == 'TXT':
            chosen_list = texts
        elif dictionary["d_type"] == 'IDS':
            chosen_list = ids
        chosen_list.append(format_elements(dictionary))

    final_list = []
    final_list.append("IDS")
    final_list.extend(ids)
    final_list.append("\nTXT")
    final_list.extend(texts)
    final_list.append("\nVAL")
    final_list.extend(numeric)
    return final_list
