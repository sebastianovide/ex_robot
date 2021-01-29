import unittest

import mars


class TestCase(unittest.TestCase):
    # TODO: errors

    def test_txtToObj_empty(self):
        inTxtLines = []
        outObj = mars.txtToObj(inTxtLines)
        self.assertEqual(outObj, {})

    def test_txtToObj_singleCommand(self):
        inTxtLines = ["5 3", "1 1 E", "RFRFRFRF"]

        outObj = mars.txtToObj(inTxtLines)
        self.assertEqual(outObj, {
            "size": {"x": 5, "y": 3},
            "commands": [
                {
                    "location": {"x": 1, "y": 1, "orientation": "E"},
                    "orders": "RFRFRFRF"
                }
            ]
        })

    def test_txtToObj_doubleCommand(self):
        inTxtLines = ["5 3", "1 1 E", "RFRFRFRF", "1 1 E", "RFRFRFRF"]

        outObj = mars.txtToObj(inTxtLines)
        self.assertEqual(outObj["size"], {"x": 5, "y": 3})
        self.assertEqual(outObj["commands"][1], {
            "location": {"x": 1, "y": 1, "orientation": "E"},
            "orders": "RFRFRFRF"
        })

    def test_objToTxtLines_singleLocation(self):
        inObj = [{"x": 1, "y": 1, "orientation": "E"}]
        outTxtLines = mars.objToTxtLines(inObj)
        self.assertEqual(outTxtLines, ["1 1 E"])

    def test_objToTxtLines_singleLocation_lost(self):
        inObj = [{"x": 1, "y": 1, "orientation": "E", "lost": True}]
        outTxtLines = mars.objToTxtLines(inObj)
        self.assertEqual(outTxtLines, ["1 1 E LOST"])

    def test_objToTxtLines_doubleLocations(self):
        inObj = [{"x": 1, "y": 1, "orientation": "E"},
                 {"x": 1, "y": 1, "orientation": "E"}]
        outTxtLines = mars.objToTxtLines(inObj)
        self.assertEqual(outTxtLines[1], "1 1 E")

    def test_moveRobots(self):
        inTxtLines = ["5 3", "1 1 E", "RFRFRFRF", "3 2 N",
                      "FRRFLLFFRRFLL", "0 3 W", "LLFFFLFLFL"]
        outTxtLinesExpected = ["1 1 E", "3 3 N LOST", "2 3 S"]

        inCmds = mars.txtToObj(inTxtLines)
        marsObj = mars.Mars()
        outObj = marsObj.moveRobots(inCmds)
        outTxtLines = mars.objToTxtLines(outObj)

        self.assertEqual(outTxtLines, outTxtLinesExpected)


if __name__ == "__main__":
    unittest.main()
