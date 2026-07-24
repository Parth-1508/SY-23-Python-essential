assignments = []

while True:
    print("-------ASSIGNMENT LIST------")
    print("MENU: \n1.ADD\n2.REMOVE\n3.SHOW\n4.EXIT")
    
    n1 = int(input("Enter your choice: "))
    
    if n1 == 1:
        task = input("Enter assignment to add: ")
        #adding assignment to the list
        assignments.append(task)
        print("Assignment added.")
        
    elif n1 == 2:
        task = input("Enter assignment to remove: ")
        #removing assignment from the list
        assignments.remove(task)
        print("Assignment removed.")
        
    elif n1 == 3:
        #displaying the list of assignments
        print("Your list:")
        print(assignments)
        
    elif n1 == 4:
        #exiting the program
        print("Exiting...")
        break