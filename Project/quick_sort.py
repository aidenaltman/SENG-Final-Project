def partition(taskList, taskListHead, taskListTail):
    
    node = taskListHead
    tracker = 0
    while node.next != None:
        node = node.next
        tracker += 1
    print("test 2.1")
    node = taskListHead
    print(tracker)
    for i in range(int(tracker//2)):
        node = node.next
    pivot = node
    print(pivot.data[1])
    print("test 2.2")
    
    while True:
        nodehead = taskListHead
        while nodehead.data[1] < pivot.data[1]:
            nodehead = nodehead.next
        nodetail = taskListTail
        while nodetail.data[1] > pivot.data[1]:
            nodetail = nodetail.prev

        if nodehead.data[1] >= nodetail.data[1]:
            break
        else:
            nodetail, nodehead = nodehead, nodetail
            nodehead = nodehead.next
            nodetail = nodetail.prev
    print("test 2.3")
    
    return nodetail





def quicksort(taskList, taskListHead, taskListTail):
    # Only attempt to sort the list segment if there are
    # at least 2 elements
    
    print("TEST 1")
    # if int(taskListTail.data[1]) <= int(taskListHead.data[1]):
    #     return

    # Partition the list segment
    print("Test 2")
    high = partition(taskList, taskListHead, taskListTail)
    print("Test 3")

    # Recursively sort the left segment
    quicksort(taskList, taskListHead, high)
    print("test 4")
    # Recursively sort the right segment
    quicksort(taskList, high.next, taskListTail)

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

