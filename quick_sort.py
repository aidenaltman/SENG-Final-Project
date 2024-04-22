from Node import Node
from LinkedList import LinkedList

def printList(taskList):
    node = taskList.head
    if node == None:
        print()
        print("No Tasks")
    else:
        print("--------------------------------------------------------")
        num = 1
        while node != None:
            print(f'{num}. {node.data[0]}')
            print(f'\tDifficulty: {node.data[1]} Time: {node.data[2]}')
            num +=1
            node = node.next
        print("--------------------------------------------------------")



def partition(start, end, num):
    pivot = end.data
    p_index = start

    current = start
    while current != end:
        print("test 2")
        if current.data[num] <= pivot[num]:
            print("test 1")
            current.data, p_index.data = p_index.data, current.data
            p_index = p_index.next
        current = current.next

    p_index.data, end.data = end.data, p_index.data
    print(p_index.prev)
    return p_index




def quicksort(start, end, num):
    if start is None or start == end or start == end.next:
        return


    pivot = partition(start, end, num)
    quicksort(start, pivot.prev, num)
    quicksort(pivot.next, end, num)

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
# printList(testList)


# sortedList = quicksort(testList.head, testList.tail, 1)
# def print_list(node):
#     while node:
#         print(node.data, end=" ")
#         node = node.next
#     print()
# print_list(sortedList)