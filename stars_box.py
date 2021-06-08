width = 5
height = 7

for i in range(0, height):
    if i == 0 or i == height -1:
        print(width * "*")
    else:
        print("*" + (width - 3) * " ", "*")

width = int(input("What is the width of the box?"))
height = int(input("What is the height of the box?"))

h = 0
w = 0

while h < height:
    if h == 0 or h == height -1:
        print(width * "*")
    else:
        print("*" + (width - 2) * " " + "*")
    h += 1


