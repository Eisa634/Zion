import random
import sys 

sub1 = random.randint(1, 10)
sub2 = random.randint(1, 10)
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
print("Maths Test")
print("1. Start Addition")
print("2. Start Subtraction")
print("3. End")
choice = input("Enter choice (Write 1 or 2): ")

if choice in ('1', '2', '3'):

    if choice == '1':
        print(num1, "+" ,num2, "=")

        answer1 = int(input("What does it equal? : "))

        num3 = num1 + num2

        if num3 == answer1 :
            print("Correct")

        elif num3 != answer1:
            print("Incorrect")

    if choice == '3':
        exit()

    if choice == '2':
        print(sub1, "-" ,sub2, "=")

        sub3 = sub1 - sub2

        subAnswer = int(input("What does it equal? : "))
    
        if sub3 == subAnswer:
            print ("Correct")

        elif sub3 != subAnswer:
                print("Incorrect")