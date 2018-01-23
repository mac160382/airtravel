"""Model for aircraft flights"""
from pprint import pprint as pp


class Flight:
    """A flight with a particular passenger aircraft."""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in {}".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code {}".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number {}".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()

        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def _get_row_letter(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]

        if letter not in seat_letters:
            raise ValueError("Invalid seat letter{}".format(letter))

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number".format(row))

        return row, letter

    def allocation_seat(self, seat, passenger):
        """
        :param seat: A seat designator such as "12C" or "12F"
        :param passenger: The passenger name
        :return:
        """
        row, letter = self._get_row_letter(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

    def reallocation_seat(self, from_seat, to_seat):
        from_row, from_letter = self._get_row_letter(from_seat)
        to_row, to_letter = self._get_row_letter(to_seat)

        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to reallocate in seat".format(from_seat))

        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def seating_plan(self):
        return self._aircraft.seating_plan()

    def seating(self):
        return self._seating

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_print):
        for passenger, seat in sorted(self._passengers_seats()):
            card_print(passenger, seat, self.number(), self.aircraft_model())

    def _passengers_seats(self):
        row_numbers, seat_letters = self.seating_plan()

        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))


class Aircraft:

    def __init__(self, registration):
        self._registration = registration

    def _registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirBusA319(Aircraft):

    def model(self):
        return "AirBus A319"

    def seating_plan(self):
        return (range(1, 23)), "ABCDEF"


class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return (range(1, 56)), "ABCDEGHJK"


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}" \
             "  Flight: {1}" \
             "  Seat: {2}" \
             "  Aircraft: {3}" \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)


def printing_information(flight):
    print(flight.aircraft_model())
    print(flight.num_available_seats())
    print(flight.make_boarding_cards(console_card_printer))


if __name__ == "__main__":
    f = Flight("BA758", AirBusA319("G-EUPT"))
    f.allocation_seat("12A", "Guido van Rossum")
    f.allocation_seat("15F", "Bjarne Stroustrup")
    f.allocation_seat("15E", "Anders Hejlsberg")
    f.allocation_seat("1C", "Jhon McCarthy")
    f.allocation_seat("1D", "Richard Hickey")
    printing_information(f)

    g = Flight("BA758", Boeing777("G-EUPT"))
    g.allocation_seat("55K", "Larry Wall")
    g.allocation_seat("33G", "Yukihiro Matsumoto")
    g.allocation_seat("4B", "Brian Kernighan")
    g.allocation_seat("4A", "Dennis Ritche")
    printing_information(g)

    
