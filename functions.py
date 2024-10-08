import json
import random


def get_dual_type_effectiveness(type1, type2, attacking_type):
    """
    :param type1: the first type of a pokemon
    :param type2: the second type of a pokemon
    :param attacking_type: the type of the move that would be used against this pokemon
    :return: None
    """
    with open("type.json", 'r') as file:
        content = file.read()

    data = json.loads(content)

    if data[type1][attacking_type] == 0.0 or data[type2][attacking_type] == 0.0:
        data["typesInQuestion"][attacking_type] = 0.0
    elif data[type1][attacking_type] == 2.0 and data[type2][attacking_type] == 2.0:
        data["typesInQuestion"][attacking_type] = 4.0
    elif data[type1][attacking_type] == 0.5 and data[type2][attacking_type] == 1.0 or \
            data[type1][attacking_type] == 1.0 and data[type2][attacking_type] == 0.5:
        data["typesInQuestion"][attacking_type] = 0.5
    elif data[type1][attacking_type] == 1.0 and data[type2][attacking_type] == 2.0 or \
            data[type1][attacking_type] == 2.0 and data[type2][attacking_type] == 1.0:
        data["typesInQuestion"][attacking_type] = 2.0
    else:
        data["typesInQuestion"][attacking_type] = 1.0

    with open("type.json", 'w') as file:
        json.dump(data, file, indent=4)


def get_single_type_effectiveness(type1, attacking_type):
    """

    :param type1: the first type of a pokemon
    :param attacking_type: the type of the move that would be used against this pokemon
    :return: None
    """
    with open("type.json", 'r') as file:
        content = file.read()

    data = json.loads(content)

    if data[type1][attacking_type] == 1.0:
        data["typesInQuestion"][attacking_type] = 1.0
    elif data[type1][attacking_type] == 2.0:
        data["typesInQuestion"][attacking_type] = 2.0
    elif data[type1][attacking_type] == 0.5:
        data["typesInQuestion"][attacking_type] = 0.5
    else:
        data["typesInQuestion"][attacking_type] = 0.0

    with open("type.json", 'w') as file:
        json.dump(data, file, indent=4)


def get_info():
    """
    gets all the information from the json file in dictionary form
    :return: the json file in dictionary format for use
    """
    with open("type.json", 'r') as file:
        content = file.read()

    data = json.loads(content)
    return data


def get_all_types():
    """
    gets the types from the json file containing their combat information
    :return: all the standard types in pokemon
    """
    data = get_info()
    types_list = list(data.keys())
    return types_list[:-1]


def get_answers():
    """

    :return: the type effectiveness attacks that would hit the type combination in question in the form of a list
    """
    data = get_info()
    answer_list = list(data["typesInQuestion"].values())
    return answer_list


def get_single_random_types():
    """

    :return: a single standard type from pokemon in set format
    """
    types = get_all_types()
    return {types[random.randint(0, len(types) - 1)]}


def get_double_random_types():
    """

    :return: two standard types from pokemon in set format
    """
    types = get_all_types()
    type1 = types[random.randint(0, len(types) - 1)]
    type2 = types[random.randint(0, len(types) - 1)]
    while type2 == type1:
        type2 = types[random.randint(0, len(types) - 1)]
    return type1, type2


if __name__ == "__main__":
    this_list = get_answers()
    print(get_answers())
