print("Welcome to the calculator !")
operator = ["+","-","*","/"]
result = 0
nb1 = 0
while True:
    if nb1 == 0:
        nb1 = int(input("Enter a number : "))
    print("Your first number is " + str(nb1))
    print("Choose an operator :")
    print("1 : +")
    print("2 : -")
    print("3 : *")
    print("4 : /")
    choice = int(input())
    if choice in [1,2,3,4]:
        nb2 = int(input("Enter another number : "))
        if choice == 1:
            print(nb1 + nb2)
            result = nb1 + nb2
        elif choice == 2:
            print(nb1 - nb2)
            result = nb1 - nb2
        elif choice == 3:
            print(nb1 * nb2)
            result = nb1 * nb2
        elif choice == 4:
            print(nb1 / nb2)
            result = nb1 / nb2
        print("Do you want to continue with the result "+str(result)+" ?")
        print("1 : Yes")
        print("2 : No i want to start a new calculation")
        choice = int(input())
        if choice == 2:
            nb1 = 0
        else:
            nb1 = result

    else:
        print("Invalid operator")
        break

