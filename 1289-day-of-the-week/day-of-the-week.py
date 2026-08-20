class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekdays = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]

        month_days = [
            31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31
        ]

        def is_leap_year(y: int) -> bool:
            return y % 400 == 0 or (
                y % 4 == 0 and y % 100 != 0
            )

        days_elapsed = 0

        # Add complete years from 1971 up to the previous year.
        for y in range(1971, year):
            days_elapsed += 366 if is_leap_year(y) else 365

        # Add complete months before the given month.
        for m in range(1, month):
            days_elapsed += month_days[m - 1]

            if m == 2 and is_leap_year(year):
                days_elapsed += 1

        # Add completed days in the current month.
        days_elapsed += day - 1

        # Friday has index 5 because the list starts with Sunday.
        return weekdays[(5 + days_elapsed) % 7]