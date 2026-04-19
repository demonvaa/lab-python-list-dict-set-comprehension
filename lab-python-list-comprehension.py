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
 

 ------------------------------
# Lab | List, Dict and Set Comprehension
## Exercise: Managing Customer Orders Optimized with Comprehension
In the previous exercise, you developed a program to manage customer orders and inventory. Now, let's take it a step further and incorporate comprehension into your code.

Follow the steps below to complete the exercise:

Review your code from the previous exercise and identify areas where you can apply comprehension to simplify and streamline your code.

Hint: Apply it to initialize inventory, updating the inventory and printing the updated inventory.

For example, in initializing the inventory, we could have:

def initialize_inventory(products):
    inventory = {product: int(input(f"Enter the quantity of {product}s available: ")) for product in products}
    return inventory

Modify the function get_customer_orders so it prompts the user to enter the number of customer orders and gathers the product names using a loop and user input. Use comprehension.

Add a new function to calculate the total price of the customer order. For each product in customer_orders, prompt the user to enter the price of that product. Use comprehension to calculate the total price. Note: assume that the user can only have 1 unit of each product.

Modify the update_inventory function to remove the product from the inventory if its quantity becomes zero after fulfilling the customer orders. Use comprehension to filter out the products with a quantity of zero from the inventory.

Print the total price of the customer order.


Your code should produce output similar to the following:

Enter the quantity of t-shirts available:  5  
Enter the quantity of mugs available:  4  
Enter the quantity of hats available:  3  
Enter the quantity of books available:  2  
Enter the quantity of keychains available:  1  
Enter the number of customer orders:  2  
Enter the name of a product that a customer wants to order:  hat  
Enter the name of a product that a customer wants to order:  keychain  

Order Statistics:  
Total Products Ordered: 2  
Percentage of Unique Products Ordered: 40.0  

Updated Inventory:  
t-shirt: 5  
mug: 4  
hat: 2  
book: 2    
Enter the price of keychain:  5  
Enter the price of hat:  10  
Total Price: 15.0  



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