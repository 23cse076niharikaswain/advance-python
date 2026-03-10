movies = {
    "Avengers": {"time": "6PM", "seats": 5},
    "Batman": {"time": "9PM", "seats": 5}
}

def show_movies():
    print("\nAvailable Movies:")
    for m in movies:
        print(m, "| Showtime:", movies[m]["time"], "| Seats:", movies[m]["seats"])

def book_ticket():
    movie = input("Enter movie name: ")
    
    if movie in movies:
        if movies[movie]["seats"] > 0:
            movies[movie]["seats"] -= 1
            print("Ticket booked for", movie)
            print("Showtime:", movies[movie]["time"])
            print("Remaining seats:", movies[movie]["seats"])
        else:
            print("Seats not available")
    else:
        print("Movie not found")

while True:
    print("\n--- Movie Ticket Booking System ---")
    print("1. Show Movies")
    print("2. Book Ticket")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_movies()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice")
