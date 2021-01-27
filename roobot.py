# Sample Input
# 5 3
# 1 1 E
# RFRFRFRF
# 3 2 N
# FRRFLLFFRRFLL
# 0 3 W
# LLFFFLFLFL
# Sample Output
# 1 1 E

def robot(inCmds):
    # TODO

    outObj = {
        "x": 1,
        "y": 1,
        "orientation": "E"
    }

    return outObj


def readInput():
    print("Enter/Paste your text. Ctrl-D (or Ctrl-Z on windows ) to save it.")
    contents = []
    while True:
        try:
            line = input('')
        except EOFError:
            break
        contents.append(line)

    # mock
    contents = """5 3
1 1 E
RFRFRFRF

3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL """

    return contents


def objToTxt(obj):
    # TODO
    return "1 1 E"


if __name__ == '__main__':
    # read input
    inTxt = readInput()

    # parse it
    # TODO
    inCmds = {}
    outObj = robot(inCmds)

    outTxt = objToTxt(outObj)

    print(outTxt)
