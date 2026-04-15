
import json

def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path

    file_path = "sequential.json"
    with open(file_path, "r") as file:
        data = json.load(file)
    if field in data.keys():
        return data[field]
    else:
        return None


def linear_search(searched_data, searched_number):
    idx = 0
    positions = []
    count = 0
    searched_dict = {}
    while idx < len(searched_data):
        if searched_data[idx] == searched_number:
            count +=1
            positions.append(idx)
        idx += 1
    searched_dict["positions"] = positions #poskladani pod dane klice do slovniku
    searched_dict["count"] = count
    return searched_dict





    return positions, count

def main():
    my_data = read_data("sequential.json","unordered_numbers")
    searched_positions = linear_search()
    print(my_data)



if __name__ == "__main__":
    main()
