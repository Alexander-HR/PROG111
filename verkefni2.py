MaxInput = 10
MinInput = 1
Left = "l"
Right = "r"
grid = ["x","x","x","x","x","x","x","x","x","x"]

def originalPos():
    while True:
        position = int(input(f"Position in [{MinInput}..{MaxInput}]"))
        if MinInput <= position <= MaxInput:
            return position -1

def getInstructions():
    for i in range(MaxInput):
        print(grid[i], end="")
    print("\nl: left \nr: right \nMove:")
    return input()
def mover(fmove, fposition):
        if fmove == Right and fposition < MaxInput - 1:
            return fposition + 1
        elif fmove == Left and fposition >= MinInput:
            return fposition - 1
        else:
            return fposition


position = originalPos()
while True:
    grid[position] = "o"
    move = getInstructions()
    position = mover(move,position)
    grid = ["x","x","x","x","x","x","x","x","x","x"]
    if move != Left and move != Right:
        break