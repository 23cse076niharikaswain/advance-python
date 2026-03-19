class OutOfStockError(Exception):
    pass

class InvalidProductIDError(Exception):
    pass

inventory = {
    "P101": 10,
    "P102": 0
}

try:
    pid = input("Enter Product ID: ")
    qty = int(input("Enter Quantity: "))

    if pid not in inventory:
        raise InvalidProductIDError("Product ID not found")

    if inventory[pid] < qty:
        raise OutOfStockError("Product out of stock")

    inventory[pid] -= qty
    print("Product purchased successfully")

except InvalidProductIDError as e:
    print(e)
except OutOfStockError as e:
    print(e)
except ValueError:
    print("Invalid quantity")
