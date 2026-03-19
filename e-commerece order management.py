stock = 5
valid_coupon = "SAVE10"

while True:
    print("\n--- E-Commerce Order System ---")
    print("1. Place Order")
    print("2. Check Stock")
    print("3. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            quantity = int(input("Enter quantity: "))

            if quantity > stock:
                raise Exception("Out of stock")

            coupon = input("Enter coupon code: ")

            if coupon != valid_coupon:
                raise Exception("Invalid coupon code")

            payment = input("Enter payment method (card/cash): ")

            if payment not in ["card", "cash"]:
                raise Exception("Invalid payment method")

            stock -= quantity
            print("Order placed successfully")

        elif choice == "2":
            print("Available stock:", stock)

        elif choice == "3":
            print("Exiting system...")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid quantity")
    except Exception as e:
        print("Error:", e)
