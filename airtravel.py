"""Model for aircraft flights"""
#from pprint import pprint as pp

from airtravel.boeing777 import Boeing777
from airtravel.airBusA319 import AirBusA319
from airtravel.flght import Flight

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



    
