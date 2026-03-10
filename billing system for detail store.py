products = {
    "apple": 50,
    "milk": 30,
    "bread": 40
}

cart = {}

def show_products():
    print("\nAvailable Products:")
    for item, price in products.items():
        print(item, "- Rs", price)

def add_product():
    name = input("Enter product name: ").lower()
    quantity = int(input("Enter quantity: "))

    if name in products:
        if name in cart:
            cart[name] += quantity
        else:
            cart[name] = quantity
        print("Product added to cart.")
    else:
        print("Product not available.")

def generate_bill():
    discount = float(input("Enter discount amount: "))
    total = 0

    print("\n--- BILL ---")
    for item, qty in cart.items():
        price = products[item] * qty
        print(item, "x", qty, "= Rs", price)
        total += price

    total = total - discount
    print("Total after discount: Rs", total)

while True:
    print("\n--- Retail Billing System ---")
    print("1. Show Products")
    print("2. Add Product to Cart")
    print("3. Generate Bill")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_products()
    elif choice == "2":
        add_product()
    elif choice == "3":
        generate_bill()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
