import datetime
from datetime import timedelta
#current_date = None

def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current date and time: ", current_date)

def calculate_future_date():
    display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = timedelta(days=number_of_days) + datetime.datetime.now()
    print(future_date)

calculate_future_date()