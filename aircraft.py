
class Aircraft:

    def __init__(self, registration):
        self._registration = registration

    def _registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


