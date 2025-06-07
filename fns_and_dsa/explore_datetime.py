from datetime import datetime, timedelta

def display_current_datetime():
    # get the current date and time and store it in current_date variable
    current_date = datetime.datetime.now()
    # format the date and time as a string and print it
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    """
    Prompt the user for a number of days, calculate, and display the future date.
    """
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.datetime.now()
        future_date = current_date + datetime.timedelta(days=days)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer value for days.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
