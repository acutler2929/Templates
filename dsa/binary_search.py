#       TAKEN FROM: CIS 226, Fall 2023
#       This is an example of a binary search
# -------------------------------------------------------------------------------------------------
# ARRAY MUST BE SORTED BEFOREHAND


def binary_search(array, look_for):
    """Perform a binary search on array to find look_for"""
    # First start out looking at the whole array
    start = 0
    end = len(array) - 1
    found = -1
    while found < 0 and start <= end:
        # Calculate midway between start and end
        midway = int((start + end) / 2)
        if array[midway] == look_for:
            # We found it!
            found = midway
        elif array[midway] < look_for:
            # Value must be to the right
            start = midway + 1
        else:
            # Value must be to the left
            end = midway - 1

    return found


numbers = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)
index = binary_search(numbers, 8)
print("The value {} is at index {}".format(8, index))
