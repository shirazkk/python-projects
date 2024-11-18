"""
Problem Statement
Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):
"""

days_in_a_year: int = 365
hours_in_a_day: int = 24
minutes_in_an_hour: int = 60
seconds_in_a_minute: int = 60

def calculate_seconds_in_a_year():
    total_seconds_in_a_year = days_in_a_year * hours_in_a_day * minutes_in_an_hour * seconds_in_a_minute
    return total_seconds_in_a_year

seconds_in_a_year = calculate_seconds_in_a_year()
print(f"There are {seconds_in_a_year:,} seconds in a year.")
