

def robot(inCmds):
    # TODO

    # mock
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

    return contents


def objToTxt(obj):
    # TODO
    # mock
    return "1 1 E"

# {
#     "size": {
#         "x": 5,
#         "y": 3
#     },
#     "commands": [
#         {
#             "location": { "x": 1, "y": 1, "orientation": "E" },
#             "orders": "FRRFLLFFRRFLL"
#         }
#     ]
# }

# 3 2 N
# FRRFLLFFRRFLL


def txtToObj(inTxtLines):
    rtnObj = {}
    if (len(inTxtLines) > 0):
        rtnObj = {"commands": []}

        line = inTxtLines[0].split(" ")
        rtnObj["size"] = {"x": int(line[0]), "y": int(line[1])}

        for i in range(1, len(inTxtLines), 2):
            line = inTxtLines[i].split(" ")
            cmd = {
                "location": {"x": int(line[0]), "y": int(line[1]), "orientation": line[2]},
                "orders": inTxtLines[i+1]
            }
            rtnObj["commands"].append(cmd)
    return rtnObj


if __name__ == '__main__':
    # read input
    inTxtLines = readInput()

    # parse it
    inCmds = txtToObj(inTxtLines)
    outObj = robot(inCmds)

    outTxt = objToTxt(outObj)

    print(outTxt)
