from airtravel.airtravel import AirBusA319

import unittest


class AirBusA319Tests(unittest.TestCase):
    """Test for the analize AirBusA319"""

    def setUp(self):
        """Fixture that create a AirBusA319 used by test methods"""
        self.airBusA319 = AirBusA319("G-EUPT")

    def test_model(self):
        self.assertEqual(self.airBusA319.model(), "AirBus A319")

    def test_seating_plan_range(self):
        self.assertEqual(self.airBusA319.seating_plan()[0], range(1, 23))

    def test_seating_plan_letters(self):
        self.assertEqual(self.airBusA319.seating_plan()[1], "ABCDEF")

    def test_num_seats(self):
        """"""
        self.assertEqual(self.airBusA319.num_seats(), 132)


if __name__ == "__main__":
    unittest.main()

