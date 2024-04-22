from Node import Node
from LinkedList import LinkedList

def partition(array, start_index, end_index, num):
    # Select the middle value as the pivot.
    midpoint = start_index + (end_index - start_index) // 2
    pivot = array[midpoint]

    # "low" and "high" start at the ends of the list segment
    # and move towards each other.
    low = start_index
    high = end_index


    # Add your code here
    while True:
        while array[low][num] < pivot[num]:
            low += 1
        
        while array[high][num] > pivot[num]:
            high -= 1

        if low >= high:
            break

        else:
            array[low], array[high] = array[high], array[low]
            low += 1
            high -= 1



    # "high" is the last index in the left segment.
    return high



def quicksort2(numbers, start_index, end_index, num):
    # Only attempt to sort the list segment if there are
    # at least 2 elements
    
    
    
    if end_index <= start_index:
        return

    # Partition the list segment
    high = partition(numbers, start_index, end_index, num)

    # Recursively sort the left segment
    quicksort2(numbers, start_index, high, num)

    # Recursively sort the right segment
    quicksort2(numbers, high + 1, end_index, num)


# Main program to test the quicksort algorithm
def quicksort(taskList, num):
    node = taskList.head
    array = []
    sortedList = LinkedList()
    
    while node != None:
        i = node.data
        array.append(i)
        node = node.next
    print(array)
    quicksort2(array, 0, len(array)-1, num)

    for j in array:
        node = Node(j)
        sortedList.append(node)

    return sortedList

# taskList = LinkedList()

# node1 = Node(("test 1", 8, 80))
# node2 = Node(("test 2", 3, 40))
# node3 = Node(("test 3", 6, 60))
# node4 = Node(("test 4", 2, 110))
# taskList.append(node4)
# taskList.append(node1)
# taskList.append(node2)

# taskList.append(node3)

# def printList(taskList):
#     node = taskList.head
#     if node == None:
#         print()
#         print("No Tasks")
#     else:
#         print("--------------------------------------------------------")
#         num = 1
#         while node != None:
#             print(f'{num}. {node.data[0]}')
#             print(f'\tDifficulty: {node.data[1]} Time: {node.data[2]}')
#             num +=1
#             node = node.next
#         print("--------------------------------------------------------")


# printList(quicksort(taskList, 2))
