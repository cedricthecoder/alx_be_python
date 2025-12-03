import datetime
from datetime import timedelta
#current_date = None
#["%Y-%m-%d %H:%M:%S"]
def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current date and time: ", current_date)

def calculate_future_date():
    display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = timedelta(days=number_of_days) + datetime.datetime.now() #importing the timedelta object and adding the current date and time to it.
    print(future_date)
    
    # Format future_date to 'YYYY-MM-DD'
    formatted_future_date = future_date.strftime("%Y-%m-%d") #New variable to accomodate the formatted date and time and the strftime method to format it.
    print(f"Future date: {formatted_future_date}")

calculate_future_date()