# Function to validate users hours and minutes input
def validate_time():
    while True:
        try:
            hours = int(input("Enter hours (0-23): "))
            minutes = int(input("Enter minutes (0-59): "))
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                return hours, minutes
            else:
                print("Invalid input. Hours must be between 0-23 and minutes must be between 0-59.")
        except ValueError:
            print("Invalid input. Please only use numbers.")

# Main function to display the validated time
def main():
    hours, minutes = validate_time()
    print(f"Valid time entered: {hours} hours and {minutes} minutes.")

if __name__ == "__main__":
    main()
