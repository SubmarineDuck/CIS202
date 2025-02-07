# Getting user input
average_speed = float(input("Enter your average speed (mph): "))
speed_limit = float(input("Enter the speed limit (mph): "))
distance_traveled = float(input("Enter the distance traveled (miles): "))

# Defining time_saved outside it's if statement
time_saved = 0

if average_speed <= speed_limit:
    print("No time saved, you were not speeding.")
else:
    # Time = Distance / Speed
    time_if_speed_limit = distance_traveled / speed_limit
    time_if_speeding = distance_traveled / average_speed

    time_saved = (time_if_speed_limit - time_if_speeding) * 60  # Converting to minutes

# Only printing if time was saved
if time_saved > 0:
    print(f"You saved {time_saved:.2f} minutes because you were speeding.")
