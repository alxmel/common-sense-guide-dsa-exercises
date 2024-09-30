""" Chapter 9, Exercise 4. Page 148 """

# Converting the Ruby Stack class in the book to Python
class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        return None  # Handle empty stack case

    def read(self):
        if not self.is_empty():
            return self.data[-1]
        return None  # Handle empty stack case

    def is_empty(self):
        return len(self.data) == 0    


def main():
    string_phrase = "abcde"
    string_reversed = ""
    new_stack = Stack()     # initialize Class
    
    # Adding the string to the Stack
    for i in string_phrase:
        new_stack.push(i)
    
    # Since Stacks are LIFO, appending the last charactre in to reverse the string
    for i in range(len(string_phrase)):
        string_reversed += new_stack.pop()
    
    print(string_reversed)

main()


