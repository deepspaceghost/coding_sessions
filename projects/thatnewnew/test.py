import os
from main import simple
import unittest


class TestHoudini(unittest.TestCase):
    """
    """

    def test_num_check(self):
        """
        """

        print("Testing function...")
        simple.num_check(34)
        if self.assertTrue(34 > 127 or 34 < 0):
            print("Number is outsite constraints.")
            print("This function is working the way it was intended.")
        else:
            print("Number is within constraints.")
            print("This function is working the way it was intended.")

    # def test_viola(self):
    #     """
    #     """

    #     print("Testing function...")
    #     simple.viola("test")
    #     self.assertTrue(os.path.exists("test"))
    #     print("This function is working the way it was intended.")


if __name__ == "__main__":
    """
    """

    unittest.main()
