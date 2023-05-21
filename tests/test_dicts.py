from utils.dicts import get_value


def test_get_value():
    dict_list = {"one": "water", "two": "fire", "three": "air"}
    assert get_value(dict_list, "one") == "water"
    assert get_value(dict_list) == 'git'
    dict_list = {}
    assert get_value(dict_list, "one", "git") == "git"
    assert get_value(dict_list, "one", "bazar") == "bazar"