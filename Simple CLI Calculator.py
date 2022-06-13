#1. ADD
#2. SUBTRACT
#3. MULTIPLY
#4. DIVIDE
#5. MODULUS

while True:

    print("Welcome!")

    print("What do you want to do?")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. MODULUS")
    print("Enter Q to Exit")

    Operation = input("Enter Your Choice: ")
    if Operation == 'q' or Operation =='Q':
        break

    if Operation == "1":
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))
        answer = num1 + num2
        print("Total is: " "{0} + {1} = {2}". format(num1,num2,answer))

    
    elif Operation == "2":
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))
        answer = num1 - num2
        print("Total is: " "{0} - {1} = {2}". format(num1,num2,answer))


    elif Operation == "3":
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))
        answer = num1 * num2
        print("Total is: " "{0} * {1} = {2}". format(num1,num2,answer))    


    elif Operation == "4":
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))
        if num2 == 0:
            print("can't divide by zero")
        else:
            answer = num1 / num2
        print("Total is: " "{0} / {1} = {2}". format(num1,num2,answer))
    

    elif Operation == "5":
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))
        answer = num1 % num2
        print("Total is: " "{0} % {1} = {2}". format(num1,num2,answer))

    else:
        print("Invalid Entry")