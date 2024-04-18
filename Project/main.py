from LinkedList import LinkedList, Node
from sortDLL import sort_linked_list

userChoice = None
taskList = LinkedList()
def printList(taskList):
    node = taskList.head
    if node == None:
        print()
        print("No tasks")
    else:
        print("--------------------------------------------------------")
        num = 1
        while node != None:
            print(f'{num}. {node.data[0]}')
            print(f'\tDifficulty: {node.data[1]} Time: {node.data[2]} minutes')
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
    print("--------------------------------------------------------")
    userChoice = input().lower()
    
    if userChoice in ("print", "print list", "1"):
        printList(taskList) 
    
    
    if userChoice in ("add", "add task", "2"):
        print("Name of task:")
        taskName = input()
        print("Task difficulty (Out of 10):")
        while True:
            taskDiff = input()
            try: 
                taskDiff = int(taskDiff)
                break
            except ValueError:
                pass
            print("Please input an integer")
        
        print("Task time (Minutes):")
        while True:
            taskTime = input()
            try: 
                taskTime = int(taskTime)
                break
            except ValueError:
                pass
            print("Please input an integer")
        
        node = Node((taskName, int(taskDiff), int(taskTime)))
        taskList.append(node)
    

    elif userChoice in ("remove task", "remove", "3"):
        if taskList.head == None:
            print()
            print("No tasks to remove")
        else:
            print()
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
        if taskList.head == None:
            print("No tasks to sort")
        else:
        
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