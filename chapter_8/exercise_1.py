""" Exercise 1 of Chapter 8, page 131 """

def main():
    array_1 = [1, 2, 3, 4, 5]
    array_2 = [0, 2, 4, 6, 8]
    print(get_intersection(array1=array_1, array2=array_2))


def get_intersection(array1: list, array2: list):
    # Create a temporary Hash Table to store the contents of one of the arrays
    temp_hash_table = {}

    # Array that returns the intersection of the two arrays
    intersection_array = []

    # Populate the Hash Table
    for i in array1:
        temp_hash_table[i] = True
    
    # If an element in array2 has a return value of True from the array1 Hash Table, append
    for j in array2:
        if temp_hash_table.get(j):
            intersection_array.append(j)
        else:
            pass
    
    return intersection_array

main()

