import math

print('''
    Welcome to the triangle area calculation tool.

       Menu: 
        1. Calculate triangle area by base and height
        2. Calculate triangle area by 2 sides and angle between them
        3. Exit
''')

def tr1():
    s = input("Enter base and height: ")
    b, h = map(float, s.split())
    print(f"{ (h * b / 2):.0f}")

def tr2():
    sec_opt = input("Enter 2 sides and angle(degrees) between them: ")
    b, c, an = map(float, sec_opt.split())
    if an < 180:
        res = math.sin(math.radians(an)) * (c * b / 2)
        print(f"{res:.0f}")
    else:
        print("Enter correct angle degrees")

def menu():
    while True:
        o_one = input("Enter menu item number: ")
        if o_one == '1':
            tr1()
        elif o_one == '2':
            tr2()
        elif o_one == '3':
            break
        else:
            print('Enter correct menu item')
menu()