from Node import Node
from LinkedList import LinkedList

def partition(start, end, num):
    pivot = end.data
    p_index = start

    current = start
    while current != end:
        if current.data[num] <= pivot[num]:
            current.data, p_index.data = p_index.data, current.data
            p_index = p_index.next
        current = current.next

    p_index.data, end.data = end.data, p_index.data
    return p_index
def quicksort(start, end, num):
    if start is None or end is None or start == end or start == end.next:
        return start, end

    pivot = partition(start, end, num)

    if pivot.prev:
        left_head, left_tail = quicksort(start, pivot.prev, num)
        left_tail.next = pivot
        pivot.prev = left_tail
    else:
        left_head = pivot

    if pivot.next:
        right_head, right_tail = quicksort(pivot.next, end, num)
        pivot.next = right_head
        right_head.prev = pivot
    else:
        right_tail = pivot

    return left_head, right_tail

def sort_linked_list(linked_list, num):
    if linked_list.head is None or linked_list.head == linked_list.tail:
        return linked_list

    sorted_head, sorted_tail = quicksort(linked_list.head, linked_list.tail, num)
    sorted_list = LinkedList()
    sorted_list.head = sorted_head
    sorted_list.tail = sorted_tail

    return sorted_list

    

# testList = LinkedList()
# node1 = Node(("test1", 8, 110))
# #taskList.append(node)
# node2 = Node(("test2", 3, 40))
# #taskList.append(node)
# node3 = Node(("test3", 6, 80))
# #taskList.append(node)
# node4 = Node(("test4", 5, 60))
# testList.append(node1)
# testList.append(node2)
# testList.append(node3)
# testList.append(node4)

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

# printList(testList)
# sortedList = sort_linked_list(testList, 2)
# printList(sortedList)










# def print_linked_list(linked_list):
#     current = linked_list.head
#     while current:
#         print(current.data, end=" ")
#         current = current.next
#     print()

# Example usage:
# Creating a linked list
# ll = LinkedList()
# ll.append(Node(3))
# ll.append(Node(2))
# ll.append(Node(5))
# ll.append(Node(4))
# ll.append(Node(1))

# print("Original Linked List:")
# print_linked_list(ll)

# sortedList = sort_linked_list(ll)

# print("Sorted Linked List:")
# print_linked_list(sortedList)
