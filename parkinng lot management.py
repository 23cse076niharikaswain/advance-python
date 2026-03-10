import time
parking_lot = {}
rate_per_hour = 20
total_spots = int(input("Enter total parking spots: "))

def vehicle_entry():
    vehicle_no = input("Enter vehicle number: ")
    if vehicle_no in parking_lot:
        print("Vehicle already parked.")
    else:
        parking_lot[vehicle_no] = time.time()
        print("Vehicle entered parking.")

def vehicle_exit():
    vehicle_no = input("Enter vehicle number: ")
    if vehicle_no not in parking_lot:
        print("Vehicle not found.")
    else:
        entry_time = parking_lot.pop(vehicle_no)
        hours = (time.time() - entry_time) / 3600
        fee = round(hours * rate_per_hour, 2)
        print("Parking fee:", fee)

def available_spots():
    print("Available spots:", total_spots - len(parking_lot))

while True:
    print("\n--- Parking Lot Menu ---")
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Check Available Spots")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        vehicle_entry()
    elif choice == "2":
        vehicle_exit()
    elif choice == "3":
        available_spots()
    elif choice == "4":
        print("Exiting system")
        break
    else:
        print("Invalid choice")
