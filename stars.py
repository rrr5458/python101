
five_stars = "*****"
count = 1
while count < 6:
    print(five_stars)
    count += 1

row_choice_square = int(input("How big is your square?"))
col_choice_square = row_choice_square
c = r = 0
empty = ""
row_builder = "*"
space = " "

while c < col_choice_square:
    empty += row_builder + space
    c += 1

print(empty)

while r < row_choice_square:
    print(empty)
    r += 1

row_choice = int(input("choose a number between 1 and 10"))
col_choice = int(input("choose a number between 1 and 10"))

rectangle_x = []
for x in range(row_choice):
    rectangle_x.append(["*"] * col_choice)
def print_board(rectangle_x):
  for row in rectangle_x:
    print(" ".join(row))

print(print_board(rectangle_x))