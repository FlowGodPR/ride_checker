# Welcome message
print("Welcome to Adventure Park Ride Checker!")

# Ask for user info
name = input("What is your name? ") 
age = int(input("How old are you? "))
height = float(input("What is your height (in inches)? "))

# Ride categories (lists of rides)
kids_rides = ["Carousel", "Mini Train", "Tea Cups"]
family_rides = ["Ferris Wheel", "Log Flume", "Bumper Cars"]
thrill_rides = ["Roller Coaster", "Drop Tower", "Loop Coaster"]

# Check if the user meets the requirements for rides
can_ride_family = age >= 8 and height >= 48
can_ride_thrill = age >= 13 and height >= 60

# Show results
print("\nHi", name, "here are the rides you can go on:")

# Kids rides (always available)
print("\nKids Rides:")
for ride in kids_rides:
    print("-", ride)

# Family rides (only if eligible)
if can_ride_family:
    print("\nFamily Rides:")
    for ride in family_rides:
        print("-", ride)
else:
    print("\nSorry, no Family Rides. You need to be at least 8 years old and 48 inches tall.")

# Thrill rides (only if eligible)
if can_ride_thrill:
    print("\nThrill Rides:")
    for ride in thrill_rides:
        print("-", ride)
else:
    print("\nSorry, no Thrill Rides. You need to be at least 13 years old and 60 inches tall.")
