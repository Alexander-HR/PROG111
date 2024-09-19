grid = ["x","x","x","x","x","x","x","x","x","x"]

position = 0 #to initiate the while loop

while position <= 0 or position > 10:
    position = int(input("Position in [1..10]"))

move = "i" #to initiate the while loop

while move != "q" and move != "Q":
    grid[position - 1] = "o"

    for i in range(10):
        print(grid[i], end="")
    print("\nl: left \nr: right \nMove:")
    move = input()

    if move == "r" and position < 10:
        grid[position - 1] = "x"
        position += 1
    elif move == "l" and position > 1:
        grid[position - 1] = "x"
        position -= 1