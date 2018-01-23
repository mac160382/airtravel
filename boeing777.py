from airtravel.aircraft import Aircraft


class Boeing777(Aircraft):
    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return (range(1, 56)), "ABCDEGHJK"
