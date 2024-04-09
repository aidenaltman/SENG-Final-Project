def partition(taskList, taskListHead, TaskListTail):
    
    
    
    
    
    
    
    
    
    
    
    node = taskListHead[1]
    tracker = 0
    while node.next != None:
        node = node.next
        tracker += 1

    node = taskListHead[1]
    for i in range(tracker/2):
        node = node.next
    pivot = node[1]

    while True:
        nodehead = taskListHead[1]
        while nodehead < pivot:



    







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
numbers = [12, 18, 3, 7, 32, 14, 91, 16, 8, 57]
print('UNSORTED:', numbers)

quicksort(numbers, 0, len(numbers) - 1)
print('SORTED:', numbers)
