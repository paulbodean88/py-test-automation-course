"""
Topics to be covered:
1. conditionals
2. loop control - for
3. loop control - while
"""

# if statement
x = int(input("Enter data: (sector 1"))
if x > 5:
    print('we are here')

# nested if
if x < 5:
    print('here')
    if input("msg ") in "popescu@gmail.com":
        print()
else:
    print('there')

# most popular if with other conditions (elif)
if x < 5:
    print('smaller')
elif x > 5:
    print('higher')
else:
    print('equal')

# understand the True and False
x, y = True, False

if x:
    print('here')

if x and y:
    print(True)
else:
    print(False)

if x or y:
    print(True)

if not x:
    print(False)
else:
    print(True)

if x in ['True', True, False]:
    print(f"I've found it on position {['True', True, False].index(x)}")