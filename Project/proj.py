from Node import Node
from LinkedList import LinkedList


userChoice = None
taskList = LinkedList()

while userChoice not in ('q', 'quit', 'exit'):
    print("--------------------------------------------------------")
    print('Please choose one of the following options:')
    print('Print List')
    print('Add task')
    print('Remove task')
    print('Sort')
    print('Quit')
    userChoice = input().lower()
    print(userChoice)
    
    
    if userChoice in ("print", "print list"):
        node = taskList.head
        if node == None:
            print()
            print("No Tasks")
        else:
            print("--------------------------------------------------------")
            while node != None:
                print(f'{node.data[0]}')
                node = node.next
            print("--------------------------------------------------------")
    
    
    if userChoice in ("add", "add task"):
        print("Name of task:")
        taskName = input().lower()
        # print("Task difficulty:")
        # taskDiff = input().lower()
        # print("Task time:")
        # taskTime = input().lower()
        
        data = (taskName, 10)#(taskName, taskDiff, taskTime)
        node = Node(data)


        taskList.append(node)

    elif userChoice in ("remove task", "remove"):
        print("Name of task to remove:")
        taskRemove = input().lower()
        node = taskList.head
        while taskRemove != node.data[0]:
            node = node.next
        taskList.remove(node)
            
        
    elif userChoice == "sort":
        print('Sort by difficulty or time?')
        taskSort = input().lower()
        if taskSort in ("diff", "difficulty"):
            pass
        elif taskSort == "time":
            pass


