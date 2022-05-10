#usr/bin/env python3

import sys
import json


def binary_search(dataset, desired_value):
    """ Function for implement binary search """

    # Edge case where dataset is empty
    if len(dataset) == 0:
        return None

    search_index = int(len(dataset) / 2)

    # edge case when the search doesnt find a pair player.
    if len(dataset) == 1 and int(dataset[0]['h_in']) != desired_value:
        return None

    # Structure of the binary search algorithm using recursion.

    if int(dataset[search_index]['h_in']) == desired_value:
        return "{} {}".format(dataset[search_index]['first_name'], dataset[search_index]['last_name'])
    elif int(dataset[search_index]['h_in']) > desired_value:
        name = binary_search(dataset[:search_index], desired_value)
    elif int(dataset[search_index]['h_in']) < desired_value:
        name = binary_search(dataset[search_index:], desired_value)
    return name


def match_input(height_match, data_2_match):

    # 1. Implementing the built-in sorting alghoritm to sort the data.

    data_2_match_sorted = sorted(data_2_match['values'], key=lambda x: int(x['h_in']))

    # 2. Defining the data structure to storage all the players pairs that we are searching.
    pair = {}

    for i in range(len(data_2_match_sorted)):

        # 3. defining the height of the player and the full name.
        height_1 = int(data_2_match_sorted[i]['h_in'])
        fullname = "{} {}".format(data_2_match_sorted[i]['first_name'], data_2_match_sorted[i]['last_name'])

        # 4. Calculus of the height to be find and using the binary search to find it.
        desired_value = height_match - height_1
        pair_player = binary_search(data_2_match_sorted, desired_value)

        # 5. Edge case where the pair is already find it in a past iteration.
        if fullname in pair.values() and pair_player in pair.keys() and pair[pair_player] == fullname \
                or fullname == pair_player:
            pair_player = None

        # 6. Edge case where the pair is made with the same player.
        if fullname == pair_player:
            pair_player = None

        # 7. Adding the pair to the data structure and print the pair.
        if pair_player is not None:
            pair[fullname] = pair_player
            print("{}     {}".format(fullname, pair_player))

    # 8. Edge case where the search doesnt find any pair.

    if len(pair) == 0:
        print('No matches found')
    else:
        return pair


if __name__ == '__main__':
    height_match = int(sys.argv[1])
    file_name = "playerlist.json"
    with open(file_name) as f:
        data_2_match = json.load(f)
    match_input(height_match, data_2_match)