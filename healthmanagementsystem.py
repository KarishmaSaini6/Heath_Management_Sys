#client names are rohan,harry,hammad
print("welcome to my health management system powerd by THE K GROUPS of fitness..")
names=["rohan","harry","hammad"]
print("kindly enter ur name sir")
name=input()

def getdate():
    import datetime
    return datetime.datetime.now()

flag=1
if name==names[0]:
    print("enter 1 to log ur data and enter 2 to retrieve ur entered data")
    choice1 = int(input())
    if choice1==1:
        print("welcome to the log section....press 1 for food and 2 for exercise")
        choice2 = int(input())
        if choice2 == 1:
            while (flag == 1):
                f = open("rohandiet.txt", "r")
                f.write(input("enter what u ate"))
                print("do u want to enter more data 1 for yes 0 for no")
                choice3 = int(input())
                if choice3 == 0:
                    flag = 0
        else:
            while (flag == 1):
                f = open("rohanexr.txt", "a")
                f.write(input("wht u did"))
                print("do u want to enter more data 1 for yes 0 for no")
                choice3 = int(input())
                if choice3 == 0:
                    flag = 0

    else:
        print("welcome to the retrive section....press 1 for food and 2 for exercise")
        choice2 = int(input())
        if choice2 == 1:
            f = open("rohandiet.txt", "r")
            content = f.read()
            print(getdate(), content)

        else:
            f = open("rohanexr.txt", "r")
            content = f.read()
            print(getdate(), content)

if name==names[1]:
    print("enter 1 to log ur data and enter 2 to retrieve ur entered data")
    choice1 = int(input())
    if choice1==1:
        print("welcome to the log section....press 1 for food and 2 for exercise")
        choice2=int(input())
        if choice2==1:
            while(flag==1):
              f=open("harry.txt","a")
              f.write(input("enter what u ate"))
              print("do u want to enter more data 1 for yes 0 for no")
              choice3=int(input())
              if choice3==0:
                  flag=0
        else:
            while(flag==1):
                f= open("harryexr.txt","a")
                f.write(input("wht u did"))
                print("do u want to enter more data 1 for yes 0 for no")
                choice3 = int(input())
                if choice3 == 0:
                    flag = 0
    else:
        print("welcome to the retrive section....press 1 for food and 2 for exercise")
        choice2 = int(input())
        if choice2 == 1:
            f = open("harrydiet.txt", "r")
            content = f.read()
            print(getdate(), content)

        else:
            f = open("harryexr.txt", "r")
            content = f.read()
            print(getdate(), content)
if name==names[2]:
    print("enter 1 to log ur data and enter 2 to retrieve ur entered data")
    choice1 = int(input())
    if choice1==1:
        print("welcome to the log section....press 1 for food and 2 for exercise")
        choice2=int(input())
        if choice2==1:
            while(flag==1):
              f=open("hammaddiet.txt","a")
              f.write(input("enter what u ate"))
              print("do u want to enter more data 1 for yes 0 for no")
              choice3=int(input())
              if choice3==0:
                  flag=0
        else:
            while(flag==1):
                f=open("hammadexr.txt","a")
                f.write(input("wht u did"))
                print("do u want to enter more data 1 for yes 0 for no")
                choice3 = int(input())
                if choice3 == 0:
                    flag = 0
    else:
        print("welcome to the retrive section....press 1 for food and 2 for exercise")
        choice2 = int(input())
        if choice2 == 1:
            f = open("hammaddiet.txt", "r")
            content = f.read()
            print(getdate(), content)

        else:
            f = open("hammadexr.txt", "r")
            content = f.read()
            print(getdate(), content)







