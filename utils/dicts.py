def get_value(collection, key="", default='git'):
    for dict_key in collection.keys():
        if dict_key == key:
            return collection[dict_key]
    return default
