#       TAKEN FROM: CIS 226, Fall 2023
#       This is an example of a linear search
# -------------------------------------------------------------------------------------------------

def linear_search(array, look_for):
    """Perform a linear search on array to find look_for"""
    for i, value in enumerate(array):
        if value == look_for:
            return i  # Found at this index
    return -1  # Not Found


numbers = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
index = linear_search(numbers, 8)
print("The value {} is at index {}".format(8, index))
