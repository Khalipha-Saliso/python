def main():
    print("Welcome to the Shopping Cart Program!")
    print("You can type 'exit' at any time to finish and see your cart.\n")

    cart = []

    while True:
        item = input("Enter the food item (or type 'exit' to finish): ").strip()

        if item.lower() == 'exit':
            break

        try:
            price_input = input(f"Enter the price for {item}: ").strip()
            if price_input.lower() == 'exit':
                break 

            price = float(price_input)
            if price < 0:
                print("Price cannot be negative. Please enter a valid price.")
                continue

            cart.append((item, price))

        except ValueError:
            print("Invalid price. Please enter a numeric value.")
            continue

    print("\nYour Shopping Cart:")
    total = 0.0

    if not cart:
        print("Your cart is empty.")
    else:
        for item, price in cart:
            print(f"- {item}: ${price:.2f}")
            total += price

        print(f"\nTotal Cost: ${total:.2f}")

if __name__ == "__main__":
    main()
