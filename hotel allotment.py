class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False
        self.guest_name = None


class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self):
        room_no = int(input("Enter room number: "))
        room_type = input("Enter room type (Single/Double/Deluxe): ")
        price = float(input("Enter room price per day: "))

        for room in self.rooms:
            if room.room_number == room_no:
                print("Room already exists.")
                return

        self.rooms.append(Room(room_no, room_type, price))
        print("Room added successfully.")

    def show_available_rooms(self):
        print("\nAvailable Rooms:")
        found = False
        for room in self.rooms:
            if not room.is_booked:
                print("Room No:", room.room_number, ", Type:", room.room_type, ", Price:", room.price)
                found = True
        if not found:
            print("No rooms available.")

    def allot_room(self):
        room_no = int(input("Enter room number to book: "))
        guest_name = input("Enter guest name: ")

        for room in self.rooms:
            if room.room_number == room_no:
                if room.is_booked:
                    print("Room already booked.")
                    return
                room.is_booked = True
                room.guest_name = guest_name
                print("Room booked successfully.")
                return

        print("Room not found.")

    def checkout_room(self):
        room_no = int(input("Enter room number for checkout: "))

        for room in self.rooms:
            if room.room_number == room_no:
                if not room.is_booked:
                    print("Room is already vacant.")
                    return
                room.is_booked = False
                room.guest_name = None
                print("Checkout successful.")
                return

        print("Room not found.")

    def show_all_rooms(self):
        print("\nAll Rooms Status:")
        for room in self.rooms:
            status = "Booked" if room.is_booked else "Available"
            print("Room", room.room_number, "|", room.room_type, "|", status)


def main():
    hotel = Hotel()

    while True:
        print("\n--- Hotel Allotment System ---")
        print("1. Add Room")
        print("2. Show Available Rooms")
        print("3. Allot Room (Check-in)")
        print("4. Checkout Room")
        print("5. Show All Rooms")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hotel.add_room()
        elif choice == "2":
            hotel.show_available_rooms()
        elif choice == "3":
            hotel.allot_room()
        elif choice == "4":
            hotel.checkout_room()
        elif choice == "5":
            hotel.show_all_rooms()
        elif choice == "6":
            print("Thank you for using the hotel system.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
