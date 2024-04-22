def partition(numbers, start_index, end_index):
    # Select the middle value as the pivot.
    midpoint = start_index + (end_index - start_index) // 2
    pivot = numbers[midpoint]

    # "low" and "high" start at the ends of the list segment
    # and move towards each other.
    low = start_index
    high = end_index


    # Add your code here
    while True:
        while numbers[low] < pivot:
            low += 1
        
        while numbers[high] > pivot:
            high -= 1

        if low >= high:
            break

        else:
            numbers[low], numbers[high] = numbers[high], numbers[low]
            low += 1
            high -= 1



    # "high" is the last index in the left segment.
    return high


def quicksort(numbers, start_index, end_index):
    # Only attempt to sort the list segment if there are
    # at least 2 elements
    if end_index <= start_index:
        return

    # Partition the list segment
    high = partition(numbers, start_index, end_index)

    # Recursively sort the left segment
    quicksort(numbers, start_index, high)

    # Recursively sort the right segment
    quicksort(numbers, high + 1, end_index)


# Main program to test the quicksort algorithm.
numbers = [12, 18, 3, 7, 32, 14, 91, 16, 110, 8, 57]
print('UNSORTED:', numbers)

quicksort(numbers, 0, len(numbers) - 1)
print('SORTED:', numbers)
