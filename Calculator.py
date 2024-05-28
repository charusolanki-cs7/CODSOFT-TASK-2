#Task 2
#Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result
g = True
while g== True:
    a= int(input("Enter the first number:"))
    b= int(input("Enter the second number:"))
    print("Which operation do you want to perform?")
    print("1.Multiplication")
    print("2.Addition")
    print("3.Subtraction")
    print("4.Division")
    print("5.Modulus")
    print("6.Floor Division")
    print("7.Exponential")
    print("8.End program")
    print("<<Press the Required key>>")
    c= int(input())
    if c==1:
        d=a*b
        print("Multiplication:",d)
    elif c==2:
        d=a+b
        print("Addition:",d)
    elif c==3:
        d=a-b
        print("Subtraction:",d)
    elif c==4:
        d=a/b
        print("Quotient:",d)
    elif c==5:
        d=a%b
        print("Modulus:",d)
    elif c==6:
        d=a//b
        print("Floor Division:",d)
    elif c==7:
        d=a**b
        print("Exponential:",d)
    elif c==8:
        print("Aborting!")
        break
    else:
        print("Error!!Not any such operation :")
#IF YOU WANT TO PERFORM ANY OPERATION AGAIN
    print("Do you want to perform any operation again?")
    print("1.Yes")
    print("2.No")
    x=int(input())
    if x==1:
        continue
    else:
        print("End Program!")
        break
print("Program Over!!")
