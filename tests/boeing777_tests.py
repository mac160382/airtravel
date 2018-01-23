from Classes.airtravel import Boeing777

import unittest


class Boeing777Tests(unittest.TestCase):
    """Test for the analize AirBusA319"""

    def setUp(self):
        """Fixture that create a AirBusA319 used by test methods"""
        self.boeing777 = Boeing777("BA758")

    def test_model(self):
        self.assertEqual(self.boeing777.model(), "Boeing 777")

    def test_seating_plan_range(self):
        self.assertEqual(self.boeing777.seating_plan()[0], range(1, 56))

    def test_seating_plan_letters(self):
        self.assertEqual(self.boeing777.seating_plan()[1], "ABCDEGHJK")

    def test_num_seats(self):
        """"""
        self.assertEqual(self.boeing777.num_seats(), 495)


if __name__ == "__main__":
    unittest.main()
    