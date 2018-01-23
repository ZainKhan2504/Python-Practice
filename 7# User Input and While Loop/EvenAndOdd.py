number = input("Enter the number, I will tell you if its odd or even: ")
number = int(number)

if number % 2 == 0:
    print("The number "+str(number)+" is even.")
else:
    print("The number " +str(number)+ " is odd.")