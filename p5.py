
a=[]
while True:
    print ("Push-1")
    print ("Pop-2")
    print ("Display-Stack −3") 
    print ("Exit-4")
    b= int(input("Enter your choice: "))
    if b==1:
        c=input("Enter any element:") 
        a. append (c)
    elif b==2:
        if a== []:
            print (" Underflow! Stack is empty...")
        else:
            print("Popped element is", a.pop())
    elif b==3:
        if a== []:
            print ("Stack is empty...")
        else:
            d= len(a)
            for i in range (d-1,-1,-1): 
                print (a[i])
    elif b==4:
        print ("End")
        break
    else:
        print("Invalid choice!")
