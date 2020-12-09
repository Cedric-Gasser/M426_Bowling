import unittest
import Bowling

class BowlingTest(unittest.TestCase):
    def test_allStrikes(self):
        Bowling.score("XXXXXXXXXXXX")
        result = Bowling.getResult()
        self.assertEqual(result, 300)


if __name__ == '__main__':
    unittest.main()
