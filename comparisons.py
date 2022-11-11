
def is_text(first_char, last_char):
    """classifies the token if its a text"""
    if first_char == '"' and last_char == '"':
        return True
    else:
        return False


def is_missing_quote_error(first_char, clast_char):
    """classifes errores when there's a missing end quote"""
    if first_char == '"' and clast_char != '"':
        return True
    else:
        return False


def is_reservada(element, reservadas):
    """determines if the element is in the given list"""
    if element in reservadas:
        return True
    else:
        return False


def is_hexadecimal(element):
    """determines if the element is hexadecimal"""
    try:
        int(element, 16)
        return True
    except ValueError:
        return False


def is_id(element):
    """determines if an element is an id"""
    if element[0].isalpha() and len(element) <= 16 and element.isalnum():
        return True
    else:
        return False
