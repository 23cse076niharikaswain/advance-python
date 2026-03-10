inventory = {}

def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))

    inventory[name] = quantity

    print("Item added")

def move_goods():
    name = input("Enter item name: ")
    qty = int(input("Enter quantity moved: "))

    if name in inventory:
        inventory[name] = inventory[name] - qty
        print("Goods moved")
    else:
        print("Item not found")

def report():
    print("\nInventory Report")

    for item in inventory:
        print(item + " : " + str(inventory[item]))

while True:
    print("\n1 Add Item")
    print("2 Move Goods")
    print("3 Inventory Report")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        move_goods()

    elif choice == "3":
        report()

    elif choice == "4":
        break
