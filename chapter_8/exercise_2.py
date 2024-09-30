""" Chapter 8, Exercise 2 on page 131 """

def main():
    test_array = ["a", "b", "c", "d", "c", "e"]
    print(get_duplicate(test_array))


def get_duplicate(array: list):
    """ Accepts an array of strings and returns the first duplicate value. O(N) """
    
    # Temporary Hash Table to store the values
    temp_hash_table = {}

    # Populating the hash
    for i in array:
        if temp_hash_table.get(i):
            # If key is already present, return the value
            return i
        else:
            # Otherwise, populate the temporary dictionary
            temp_hash_table[i] = True

main()

