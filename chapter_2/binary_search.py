""" Testing Binary Search """
def main():
    perform_binary_search(generate_array(100), 73)

def generate_array(n: int):
    """ Function that creates an ordered array """
    # Binary Search ONLY works with Ordered Arrays
    ordered_array = []

    for i in range(n):
        ordered_array.append(i)
    
    return ordered_array

def perform_binary_search(ordered_array: list, value: int):
    """ Performs Binary Search on provided list for provided value """
    # keeping track of steps taken
    steps_count = 0

    # keeping track of the starting point
    start_point = 0

    # keeping track of the ending point
    end_point = len(ordered_array) - 1

    # getting the middle point to begin the search in the middle
    middle_point = int((start_point + end_point) / 2)

    # Only repeat as many times as the array is long.
    while start_point <= end_point:
        # incrementing steps for every step taken
        steps_count += 1

        # Performing the binary search. If found, exit and return
        if ordered_array[middle_point] == value:
            print(f"Value found! Steps taken: {steps_count}")
            return 0
        elif ordered_array[middle_point] <= value:
            start_point = middle_point + 1
            middle_point = int((start_point + end_point) / 2)
        elif ordered_array[middle_point] >= value:
            end_point = middle_point - 1
            middle_point = int((start_point + end_point) / 2)
    
    # If the loop is done and we haven't found the value yet, then it's not in the array
    print("Value not in the array.")
    return 1

main()


"""
# ChatGPT implementation, with minor changes:

#####################################################
def main():
    perform_binary_search(generate_array(100), 73)

def generate_array(n: int):
    # Binary Search ONLY works with Ordered Arrays
    ordered_array = [i for i in range(n)]
    return ordered_array

def perform_binary_search(ordered_array: list, value: int):
    # keeping track of steps taken
    steps_count = 0

    # keeping track of the starting point
    start_point = 0

    # keeping track of the ending point
    end_point = len(ordered_array) - 1

    # getting the middle point to begin the search in the middle
    middle_point = (start_point + end_point) // 2

    # Only repeat as many times as the array is long.
    while start_point <= end_point:
        # incrementing steps for every step taken
        steps_count += 1

        # Performing the binary search. If found, exit and return
        if ordered_array[middle_point] == value:
            print(f"Value found! Steps taken: {steps_count}")
            return 0
        elif ordered_array[middle_point] < value:
            start_point = middle_point + 1
        else:
            end_point = middle_point - 1
        
        # Update middle_point after changing start or end
        middle_point = (start_point + end_point) // 2
    
    # If the loop is done and we haven't found the value yet, then it's not in the array
    print("Value not in the array.")
    return 1

main()
#####################################################

Key Changes:
1. Integer Division (//): Used integer division to ensure you always get integer indices.
2. Simplified Logic: Removed redundant condition in the elif block. Since you're already comparing for equality above, you only need to check ordered_array[middle_point] < value or go to the else block if it's greater.

This should now be working well! Let me know how it runs or if any adjustments are needed.


####
The reason we can do #2 is because 'middle_point' variable definition is already performing the required logic to get the middle point,
by adding the start and end points and dividing by 2 and converting it to an int
###


"""


