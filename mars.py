class MarsWithoutLogic:
    def __init__(self):
        self.scents = {}

    def executeCommand(self, order, x, y, orientation):
        return x, y, orientation, False

    def moveRobots(self, inCmds):
        outObj = []
        self.size = inCmds["size"]
        for command in inCmds["commands"]:
            lost = False
            x = command["location"]["x"]
            y = command["location"]["y"]
            orientation = command["location"]["orientation"]

            for order in command["orders"]:
                if not lost:
                    x, y, orientation, lost = self.executeCommand(
                        order, x, y, orientation)

            obj = {"x": x, "y": y, "orientation": orientation}
            if lost:
                obj["lost"] = True

            outObj.append(obj)

        return outObj


class Mars(MarsWithoutLogic):
    def __init__(self):
        super().__init__()
        self.logic = {
            "L": self.L,
            "R": self.R,
            "F": self.F
        }
        self.ORIENTATIONS = {
            "N": {"dx": 0, "dy": 1},
            "E": {"dx": 1, "dy": 0},
            "S": {"dx": 0, "dy": -1},
            "W": {"dx": -1, "dy": 0},
        }

    def executeCommand(self, order, x, y, orientation):
        return self.logic[order](x, y, orientation)

    def changeOrientation(self, orientation, delta):
        orientationIdx = list(self.ORIENTATIONS).index(orientation) + delta
        if orientationIdx < 0:
            orientationIdx += 4
        if orientationIdx > 3:
            orientationIdx -= 4

        return list(self.ORIENTATIONS)[orientationIdx]

    def L(self, x, y, orientation):
        orientation = self.changeOrientation(orientation, -1)
        return x, y, orientation, False

    def R(self, x, y, orientation):
        orientation = self.changeOrientation(orientation, 1)
        return x, y, orientation, False

    def F(self, x, y, orientation):
        lost = False

        next_x = x + self.ORIENTATIONS[orientation]["dx"]
        next_y = y + self.ORIENTATIONS[orientation]["dy"]

        if next_x >= self.size["x"] or next_x < 0 or next_y > self.size["y"] or next_y < 0:
            coordsKey = str(x) + "_" + str(x)

            if (coordsKey) not in self.scents:
                lost = self.scents[coordsKey] = True
        else:
            x = next_x
            y = next_y

        return x, y, orientation, lost


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

    # new simulation.
    mars = Mars()

    # simulation
    outObj = mars.moveRobots(inCmds)

    # convert result in list of text
    outTxtLines = objToTxtLines(outObj)

    for textLine in outTxtLines:
        print(textLine)
