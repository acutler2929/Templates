#       TAKEN FROM: CIS 226, Fall 2023
#       This is an example of a selection sort
# -------------------------------------------------------------------------------------------------

def swap(array, index1, index2):
    """Swap values at given indexes in given array"""
    # Store first in temp
    temp = array[index1]
    # Replace first with second
    array[index1] = array[index2]
    # Use temp to replace second
    array[index2] = temp

    # Remember arrays are passed by reference
    # so the actual array will be updated.


def selection_sort(array):
    """Sort array in ascending order using Selection Sort"""
    # Iterate Marker A from 0 to end of array - 1
    for marker_a in range(len(array) - 1):
        # Start Marker C at Marker A to represent lowest value
        marker_c = marker_a

        # Iterate Marker B from Marker A to end of array
        for marker_b in range(marker_a, len(array)):
            # Keep track of lowest value
            if array[marker_b] < array[marker_c]:
                marker_c = marker_b

        # Swap if they aren't the same
        if marker_a != marker_c:
            swap(array, marker_a, marker_c)

    # Print sorted array
    print(array)


numbers = [9, 5, 3, 6, 8, 1, 0, 2, 4, 7]
print(numbers)
selection_sort(numbers)
