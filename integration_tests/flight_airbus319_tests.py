from airtravel.flght import Flight
from airtravel.airBusA319 import AirBusA319

import unittest


class Boeing777Tests(unittest.TestCase):

    def setUp(self):
        self.flight_airbus319 = Flight("BA758", AirBusA319("G-EUPT"))
        self.seat = "12A"
        self.passenger = "Guido van Rossum"

    def test_number(self):
        self.assertEqual(self.flight_airbus319.number(), "BA758")

    def test_airline(self):
        self.assertEqual(self.flight_airbus319.airline(), "BA")

    def test_aircraft_model(self):
        self.assertEqual(self.flight_airbus319.aircraft_model(), "Boeing 777")

    def test_seating_plan_rows(self):
        self.assertEqual(self.flight_airbus319.seating_plan()[0], range(1, 56))

    def test_seating_plan_letters(self):
        self.assertEqual(self.flight_airbus319.seating_plan()[1], "ABCDEGHJK")

    def test_seating(self):
        rows, seats = self.flight_airbus319.seating_plan()
        seat = [None] + [{letter: None for letter in seats} for _ in rows]
        self.assertEqual(self.flight_airbus319.seating(), seat)

    def test_num_available_seats(self):
        self.assertEqual(self.flight_airbus319.num_available_seats(), 495)

    def test_allocation_seat(self):
        self.flight_airbus319.allocation_seat(self.seat, self.passenger)
        self.assertEqual(self.flight_airbus319.seating()[12]["A"], self.passenger)

    def test_allocation_seat_raise_error_when_row_not_exist(self):
        self.assertRaises(ValueError, self.flight_airbus319.allocation_seat, "135B", self.passenger)

    def test_allocation_seat_raise_error_when_letter_not_exist(self):
        self.assertRaises(ValueError, self.flight_airbus319.allocation_seat, "12Z", self.passenger)

    def test_allocation_seat_raise_error_when_allocate_the_same_seat(self):
        self.flight_airbus319.allocation_seat(self.seat, self.passenger)
        self.assertRaises(ValueError, self.flight_airbus319.allocation_seat, self.seat, self.passenger)

    def test_reallocation_seat(self):
        self.flight_airbus319.allocation_seat(self.seat, self.passenger)
        self.flight_airbus319.reallocation_seat(self.seat, "12B")
        self.assertEqual(self.flight_airbus319.seating()[12]["A"], None)
        self.assertEqual(self.flight_airbus319.seating()[12]["B"], self.passenger)

    def test_reallocation_seat_raise_error_when_from_seat_is_None(self):
        self.assertRaises(ValueError, self.flight_airbus319.reallocation_seat, "12C", "12B")

    def test_reallocation_seat_raise_error_when_to_seat_is_occupied(self):
        self.flight_airbus319.allocation_seat(self.seat, self.passenger)
        self.flight_airbus319.allocation_seat("12B", self.passenger)
        self.assertRaises(ValueError, self.flight_airbus319.reallocation_seat, self.seat, "12B")


if __name__ == "__main__":
    unittest.main()
