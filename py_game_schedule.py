from datetime import date, timedelta

class Season:
    def __init__(self, start_date):
        self.start_date = start_date
        self.end_date = start_date + timedelta(weeks=26)

    def print_game_schedule(self):
        for i in range(0, 26, 2):
            wednesday = self.start_date + timedelta(weeks=i, days=0)
            sunday = self.start_date + timedelta(weeks=i, days=4)
            print("Utakmice - Srijeda: ", wednesday, '&'  " Nedjelja: ", sunday, '\n')

start_date = date.today() + timedelta(days=1)  

season = Season(start_date)
season.print_game_schedule()