from Node import Node
from LinkedList import LinkedList
from sortDLL import sort_linked_list

userChoice = None
taskList = LinkedList()
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




while userChoice not in ('q', 'quit', 'exit', "5"):
    print("--------------------------------------------------------")
    print('Please choose one of the following options:')
    print('1. Print List')
    print('2. Add task')
    print('3. Remove task')
    print('4. Sort')
    print('5. Quit')
    userChoice = input().lower()
    #print(userChoice)
    
    
    if userChoice in ("print", "print list", "1"):
        printList(taskList) 
    
    
    if userChoice in ("add", "add task", "2"):
        print("Name of task:")
        taskName = input()
        print("Task difficulty (Out of 10):")
        taskDiff = input()
        print("Task time (Minutes):")
        taskTime = input()
        
        node = Node((taskName, int(taskDiff), int(taskTime)))
        taskList.append(node)

        # node = Node(("test1", 8, 110))
        # taskList.append(node)
        # node = Node(("test2", 3, 40))
        # taskList.append(node)
        # node = Node(("test3", 6, 80))
        # taskList.append(node)
        # node = Node(("test4", 2, 60))
        # taskList.append(node)
        # taskList.append(node1)
        # taskList.append(node2)
        # taskList.append(node3)

    elif userChoice in ("remove task", "remove", "3"):
        print("Name of task to remove:")
        printList(taskList)
        taskRemove = input().lower()
        node = taskList.head
        
        while taskRemove != node.data[0].lower():
            if node.next == None:
                print("That task is not on the list.")
                break
            node = node.next
        if node.data[0] == taskRemove:
            taskList.remove(node)
            
        
    elif userChoice in ("sort", "4"):
        print('Sort by difficulty or time?')
        taskSort = input().lower()
        if taskSort in ("diff", "difficulty"):
            sortList = taskList
            sortedList = sort_linked_list(sortList, 1)
            printList(sortedList)

        elif taskSort == "time":
            sortList = taskList
            sortedList = sort_linked_list(sortList, 2)
            printList(sortedList)
            

