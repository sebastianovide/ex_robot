scents = {}
ORIENTATIONS = {
    "N": {"dx": 0, "dy": 1},
    "E": {"dx": 1, "dy": 0},
    "S": {"dx": 0, "dy": -1},
    "W": {"dx": -1, "dy": 0},
}


def changeOrientation(orientation, delta):
    orientationIdx = list(ORIENTATIONS).index(orientation) + delta
    if orientationIdx < 0:
        orientationIdx += 4
    if orientationIdx > 3:
        orientationIdx -= 4

    return list(ORIENTATIONS)[orientationIdx]


def L(x, y, orientation, size):
    orientation = changeOrientation(orientation, -1)
    return x, y, orientation, False


def R(x, y, orientation, size):
    orientation = changeOrientation(orientation, 1)
    return x, y, orientation, False


def F(x, y, orientation, size):
    lost = False

    next_x = x + ORIENTATIONS[orientation]["dx"]
    next_y = y + ORIENTATIONS[orientation]["dy"]

    if next_x >= size["x"] or next_x < 0 or next_y > size["y"] or next_y < 0:
        coordsKey = str(x) + "_" + str(x)

        if (coordsKey) not in scents:
            lost = scents[coordsKey] = True
    else:
        x = next_x
        y = next_y

    return x, y, orientation, lost


commandLogic = {
    "L": L,
    "R": R,
    "F": F
}


def moveRobots(inCmds, commandLogic):
    outObj = []
    size = inCmds["size"]
    for command in inCmds["commands"]:
        lost = False
        x = command["location"]["x"]
        y = command["location"]["y"]
        orientation = command["location"]["orientation"]

        for order in command["orders"]:
            if not lost:
                x, y, orientation, lost = commandLogic[order](
                    x, y, orientation, size)

        obj = {"x": x, "y": y, "orientation": orientation}
        if lost:
            obj["lost"] = True

        outObj.append(obj)

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


def objToTxtLines(obj):
    txtLines = []
    for o in obj:
        line = str(o["x"]) + " " + str(o["y"]) + " " + o["orientation"]
        if "lost" in o:
            line += " LOST"
        txtLines.append(line)

    return txtLines


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

    # simulation
    outObj = moveRobots(inCmds, commandLogic)

    # convert result in list of text
    outTxtLines = objToTxtLines(outObj)

    for textLine in outTxtLines:
        print(textLine)
