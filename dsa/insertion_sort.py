#       TAKEN FROM: CIS 226, Fall 2023
#       This is an example of an insertion sort
# -------------------------------------------------------------------------------------------------

def insertion_sort(array):
    """Sort array in ascending order using Insertion Sort"""
    # Iterate Marker A from 1 to end of array
    for marker_a in range(1, len(array)):
        # Store unsorted value to be moved later
        unsorted_value = array[marker_a]
        # Start Marker B at Marker A to represent scan start
        marker_b = marker_a

        # Move Marker B left to where unsorted value should go
        while marker_b > 0 and array[marker_b-1] > unsorted_value:
            # Shift elements to the right and move left
            array[marker_b] = array[marker_b-1]
            marker_b -= 1

        # Move unsorted value to correct spot
        array[marker_b] = unsorted_value

    # Print sorted array
    print(array)


numbers = [9, 5, 3, 6, 8, 1, 0, 2, 4, 7]
print(numbers)
insertion_sort(numbers)
