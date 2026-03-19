available_seats = 5

try:
    name = input("Enter Passenger Name: ")
    age = int(input("Enter Age: "))

    if name == "" or age <= 0:
        raise Exception("Invalid passenger details")

    seats = int(input("Enter number of seats: "))

    if seats > available_seats:
        raise Exception("Seats not available")

    payment = input("Enter payment status (success/fail): ")

    if payment != "success":
        raise Exception("Payment failure")

    available_seats -= seats
    print("Flight booked successfully")

except ValueError:
    print("Invalid input type")
except Exception as e:
    print("Error:", e)
