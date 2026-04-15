
import json
import time
from generators import unordered_sequence, ordered_sequence
import matplotlib.pyplot as plt


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
    return positions, count

def binary_search(searched_data, searched_number):
    left = 0
    right = len(searched_data) - 1
    while left <= right:
        middle = (left + right) // 2
        if searched_data[middle] == searched_number:
            return middle
        elif searched_data[middle] < searched_number:
            left = middle + 1
        elif searched_data[middle] > searched_number:
            left = middle - 1
    return None
# je to slozitost (log n)

def test_complexit(list_of_n):
    ordered_data = ordered_sequence()
    duration = 0
    repetion = 100
    for n in list_of_n:
        unordered_data = unordered_sequence()
        found_number = linear_search(unordered_data, number)

    plt.plot(list_of_n, times_linear) # nedodelano / test complexity
    plt.plot(list_of_n, times_binary)

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas [s]")
    plt.title("Ukázkový graf měření")
    plt.show()


def pattern_search(sequence, pattern):
    indexy = {}
    while
    return indexy


def main():
    my_data = read_data("sequential.json","unordered_numbers")
    found_number = linear_search(my_data, 0)
    START_time = time.perf_counter()
    found_numberb = binary_search(my_data, 18)
    end_time = time.perf_counter()
    duration = end_time - START_time
    print(duration)                # dam timer pred funkci a po funkci


if __name__ == "__main__":
    main()
