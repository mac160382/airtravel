from Classes.airtravel import Flight, Boeing777

import unittest


class Boeing777Tests(unittest.TestCase):

    def setUp(self):
        self.flight_boeing777 = Flight("BA758", Boeing777("G-EUPT"))

    def test_number(self):
        self.assertEqual(self.flight_boeing777.number(), "BA758")

    def test_airline(self):
        self.assertEqual(self.flight_boeing777.airline(), "BA")

    '''
    def test_aircraft_model(self):
        return self._aircraft.model()

    def test_seating_plan(self):
        return self._aircraft.seating_plan()

    def test_seating(self):
        return self._seating
    '''


if __name__ == "__main__":
    unittest.main()
