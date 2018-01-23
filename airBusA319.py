from airtravel.aircraft import Aircraft


class AirBusA319(Aircraft):
    def model(self):
        return "AirBus A319"

    def seating_plan(self):
        return (range(1, 23)), "ABCDEF"