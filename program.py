
to_do_list = []

def view_task():
    x = len(to_do_list)
    for i in range (x):
        print("\n")
        print(to_do_list[i])

def add_task():
    print("how many task do you want to add")
    b=int(input("enter the number of task:  "))
    for i in range (b):
        a = input("enter your task  ")
        to_do_list.append(a)
        print("task added sucessfully  ")
        x = len(to_do_list)
def remove_task():
    r = int(input("enter the task number you want to remove:  "))-1
    to_do_list.pop(r)
    print("task removed sucessfully  ")
    
def main():
    while True:
        print("welcome to your to do list what do you want to do  ")
        print("1 view your to do list  ")
        print("2 add a new task  ")
        print("3 remove a task  ")
        print("4 quit")
        d =  input("what do u want to do 1,2,3,4:  ")
        if d == "1":
            view_task()
        elif d == "2":
            add_task()
        elif d == "3":
            remove_task()
        elif d == "4":
            break
        else:
            print('enter a valid input')

main()
