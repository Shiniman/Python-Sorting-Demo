# main.py
"""
Python Sorting Demo
File contains 2 functions
- sort_integers(sorts numbers in ascending order (descending=false))
- sort_strings(sorts strings in alphabetical order (reverse=false))
"""

# Demo Comment

def sort_integers(numbers, descending=False):

    # Sort Integer Branch Example: Used python's built-in sorted() function 
    return sorted(numbers, reverse=descending)

def sort_strings(strings, reverse=False):

    # Sort String Branch Example: Capitalized words sort before lowercase words when alphabetized 
    return sorted(strings, reverse=reverse)

def run_sorter():
    int_set = [4, 7, 9, 2, 1, 4]
    str_set = ["apple", "orange", "banana", "Apple", "banana"]

    print("Integer sort (ascending): ", sort_integers(int_set))
    print("Integer sort (descending): ", sort_integers(int_set, descending=True))
    print("String sort (alphabet): ", sort_strings(str_set))
    print("String sort (reverse alphabet): ", sort_strings(str_set, reverse=True))

if __name__ == "__main__":
    run_sorter()
