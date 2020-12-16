import unittest
import Bowling


class BowlingTest(unittest.TestCase):
    def test_allStrikes(self):
        Bowling.score("XXXXXXXXXXXX")
        result = Bowling.getResult()
        self.assertEqual(300, result)

    def test_allSpares(self):
        Bowling.score("3/4/9/2/9/0/-/-/1/6/8")
        result = Bowling.getResult()
        self.assertEqual(139, result)

    def test_hittinNothingAtAll(self):
        Bowling.score("--00--00--00--00--00")
        result = Bowling.getResult()
        self.assertEqual(0, result)

    def testException_moreThan10Pins(self):
        with self.assertRaises(Exception) as ex:
            Bowling.score("99999999999999999999")
        the_exception = ex.exception
        self.assertEqual(str(Exception("More than 10 pins?!")), str(the_exception))


if __name__ == '__main__':
    unittest.main()
