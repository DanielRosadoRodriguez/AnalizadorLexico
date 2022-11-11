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
