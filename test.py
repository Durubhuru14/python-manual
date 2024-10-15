from datetime import datetime

def get_date_from_user():
    user_input = input("Enter a date (YYYY-MM-DD): ")
    
    try:
        # Attempt to parse the user input
        parsed_date = datetime.strptime(user_input, "%Y-%m-%d")
        print(f"Successfully parsed date: {parsed_date.date()}")
    except ValueError as ve:
        # Handle the case where the date is invalid
        print(f"Error: {ve}. Please enter a valid date in the format YYYY-MM-DD.")
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An unexpected error occurred: {e}")

# Example usage
get_date_from_user()
