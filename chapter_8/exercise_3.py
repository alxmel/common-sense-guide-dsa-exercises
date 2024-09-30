""" Chapter 8, exercise 3 page 131 """

def main():
    string_phrase = "the quick brown box jumps over a lazy dog"
    print(get_missing_letter(string_phrase))

def get_missing_letter(phrase: str):
    """ Returns the single missing letter from string. O(N) """
    alphabet = {
        "a": False,
        "b": False,
        "c": False,
        "d": False,
        "e": False,
        "f": False,
        "g": False,
        "h": False,
        "i": False,
        "j": False,
        "k": False,
        "l": False,
        "m": False,
        "n": False,
        "o": False,
        "p": False,
        "q": False,
        "r": False,
        "s": False,
        "t": False,
        "u": False,
        "v": False,
        "w": False,
        "x": False,
        "y": False,
        "z": False
    }

    # Temp array to hold only letters
    letters_only_array = []

    # looping through the string, and pulling out only the letters from the string in lowercase
    for i in phrase:
        if i.isalpha():
            letters_only_array.append(i.lower())
    
    # Looping through phrase and updating the value from False to True
    for j in letters_only_array:
        alphabet[j] = True
    
    # Iterate through the Keys and return the single False value
    for k in alphabet.keys():
        if not (alphabet.get(k)):
            return k

main()
