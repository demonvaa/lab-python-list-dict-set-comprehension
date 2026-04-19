def initialize_inventory(products):
    inventory = {
        producto: int(input(f"Enter the quantity of {producto} available: "))
        for producto in products
    }
    return inventory


def get_customer_orders(product_list):
    number_of_orders = int(input("Enter the number of customer orders: "))
    customer_orders = []

    while len(customer_orders) < number_of_orders:
        item = input("Enter product name: ")

        if item in product_list:
            customer_orders.append(item)
        else:
            print("That product is not in the product list. Try again.")

    return customer_orders


def update_inventory(customer_orders, inventory):
    updated = {
        product: (qty - customer_orders.count(product))
        for product, qty in inventory.items()
    }

    updated = {product: qty for product, qty in updated.items() if qty > 0}

    return updated


def print_updated_inventory(updated_inventory):
    for product, qty in updated_inventory.items():
        print(f"{product}: {qty}")


def calculate_order_statistics(customer_orders, product_list):
    total = len(customer_orders)
    unique = len(set(customer_orders))
    percentage = (unique / len(product_list)) * 100
    return unique, percentage


def print_order_statistics(order_statistics):
    valor1, valor2 = order_statistics
    print(f"Total Products Ordered: {valor1}")
    print(f"Percentage of Unique Products Ordered: {valor2}")


def calculate_total_price(customer_orders):
    # Convertimos la lista en diccionario de cantidades
    quantities = {
        product: customer_orders.count(product)
        for product in set(customer_orders)
    }

    prices = {
        product: float(input(f"Introduce el precio de {product}: "))
        for product in quantities
    }

    total = sum(
        prices[product] * quantities[product]
        for product in quantities
    )

    return prices, quantities, total


def print_total_price(prices, quantities, total):
    print("\n--- FACTURA ---")
    for product in prices:
        print(f"{product}: {quantities[product]} uds × {prices[product]} €/ud")

    print(f"\nTOTAL: {total} euros")


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------

lista_productos = ['t-shirt', 'mug', 'hat', 'book', 'keychain']

inventory = initialize_inventory(lista_productos)

customer_orders = get_customer_orders(lista_productos)

order_statistics = calculate_order_statistics(customer_orders, lista_productos)
print_order_statistics(order_statistics)

print("\nUpdated Inventory:")
inventory = update_inventory(customer_orders, inventory)
print_updated_inventory(inventory)

prices, quantities, total = calculate_total_price(customer_orders)
print_total_price(prices, quantities, total)
 
