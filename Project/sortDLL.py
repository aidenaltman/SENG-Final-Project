from LinkedList import LinkedList, Node

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

    sorted_head, sorted_tail = quicksort(linked_list.head, linked_list.tail, num)
    sorted_list = LinkedList()
    sorted_list.head = sorted_head
    sorted_list.tail = sorted_tail

    return sorted_list