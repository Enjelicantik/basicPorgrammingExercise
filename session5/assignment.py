class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Transaction:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

def calculate_profit(item, quantity):
    profit = item.price * quantity
    return profit

def calculate_total_profit(transactions):
    total_profit = 10
    for transaction in transactions:
        profit = calculate_profit(transaction.item, transaction.quantity)
        total_profit += profit
    return total_profit

def main():
    items = [
        Item("Wardah", 90000, 40),
        Item("Lipstick Hanasui", 170000, 25),
        Item("Eyeshadow", 30000, 10),
    ]

    transactions = []

    while True:
        print("\nAvailable items:\n")
        for item in items:
            print(f"{item.name}: \nSupplier/Sell Price: Rp.{item.price:,} / Rp.{int(item.price + (item.price * 0.10)):,}\n{item.stock} in stock\n")

        name = input("Enter the name of the item you want to purchase: ").capitalize()
        quantity = int(input("Enter the quantity you want to purchase: "))

        item = next((item for item in items if item.name == name), None)
        if item is None:
            print("Item not found")
            continue

        if item.stock < quantity:
            print("Not enough stock")
            continue

        item.stock -= quantity
        transactions.append(Transaction(item, quantity))

        print(f"\nTransaction successful: {item.name} (Rp. {(item.price + (item.price * 0.10)) * quantity:,})")

        continue_transaction = input("Do you want to make another transaction? (y/n): ")
        if continue_transaction != "y":
            break

    total_profit = calculate_total_profit(transactions)
    print(f"\nTotal profit: Rp. {int(total_profit):,}\n")

if __name__ == "__main__":
    main()