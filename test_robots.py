import unittest

import robots

# Sample Input
# 5 3
# 1 1 E
# "RFRFRFRF"
# 3 2 N
# FRRFLLFFRRFLL
# 0 3 W
# LLFFFLFLFL
# Sample Output
# 1 1 E


class TestCase(unittest.TestCase):
    # TODO: errors

    def test_txtToObj_empty(self):
        inTxtLines = []
        outObj = robots.txtToObj(inTxtLines)
        self.assertEqual(outObj, {})

    def test_txtToObj_singleCommand(self):
        inTxtLines = ["5 3", "1 1 E", "RFRFRFRF"]

        outObj = robots.txtToObj(inTxtLines)
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

        outObj = robots.txtToObj(inTxtLines)
        self.assertEqual(outObj["size"], {"x": 5, "y": 3})
        self.assertEqual(outObj["commands"][1], {
            "location": {"x": 1, "y": 1, "orientation": "E"},
            "orders": "RFRFRFRF"
        })


if __name__ == "__main__":
    unittest.main()
