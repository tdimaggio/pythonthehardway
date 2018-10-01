#Cord Calculator for Wood
print("Welcome to the cord calculator")
#while statements error handle if int or float isn't used
while True:
    try:
        length = input("Please enter the length of stack in feet:")
        flength = float(length)
        break
    except ValueError:
        print("Please enter feet as number!")
while True:
    try:
        depth = input("Please enter the depth of stack in feet:")
        fdepth = float(depth)
        break
    except ValueError:
        print("Please enter feet as number!")
while True:
    try:
        height = input("Please enter the height of the stack in feet:")
        fheight = float(height)
        break
    except ValueError:
        print("Please enter feet as number!")

def computesqft(l,d,h) :
    sqrft = flength * fdepth * fheight
    return sqrft

answ = computesqft(flength,fdepth,fheight)
print("Square footage is:",answ,"Sqaure Feet")
print("Total cords:",answ / 128,"Cords")
