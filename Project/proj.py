from Node import Node
from LinkedList import LinkedList
from quicksortarray import quicksort

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
        
        data = (taskName, taskDiff, taskTime)
        node = Node(data)
        taskList.append(node)

    elif userChoice in ("remove task", "remove", "3"):
        print("Name of task to remove:")
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
            printList(quicksort(taskList, 1))

        elif taskSort == "time":
            printList(quicksort(taskList, 2))

