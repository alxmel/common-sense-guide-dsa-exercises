""" Chapter 8, Exercise 4. Page 131 """

def main():
    input_string = "minimum"
    print(return_non_dupe(input_string))

def return_non_dupe(phrase: str) -> str:
    """ Returns the first non-duplicated character in a string. O(N) """
    temp_hash_table = {}

    # Populating the temp hash table with the input
    for i in phrase:
        if i not in temp_hash_table:
            temp_hash_table[i] = 1
        else:
            temp_hash_table[i] += 1
    
    # iterate through the phrase again to return the first value that only ocurred once
    for j in phrase:
        if temp_hash_table[j] == 1:
            return j

main()
