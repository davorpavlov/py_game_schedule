from datetime import date, timedelta

class Season:
    def __init__(self, start_date, num_weeks):
        self.start_date = start_date
        self.num_weeks = num_weeks
        self.end_date = start_date + timedelta(weeks=num_weeks)

    def print_game_schedule(self):
        for i in range(0, self.num_weeks, 2):
            wednesday = self.start_date + timedelta(weeks=i, days=0)
            sunday = self.start_date + timedelta(weeks=i, days=4)
            print("Utakmice - Srijeda: ", wednesday, " & Nedjelja: ", sunday, '\n')

num_weeks = int(input("Unesite broj tjedana za koje želite da traje sezona: "))
start_date = date.today() + timedelta(days=1)  # sezona pocinje sutra, 12.4.2023

season = Season(start_date, num_weeks)
season.print_game_schedule()