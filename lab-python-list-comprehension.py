def initialize_inventory(products): # parametro de entrada una lista
    inventory = {
        producto: int(input(f"Enter the quantity of {producto} available: "))
        for producto in products
    }
    return inventory # devuelve un inventario

def get_customer_orders(product_list):
    number_of_orders = int(input("Enter the number of customer orders: "))

    orders = [
        input("Enter product name: ")
        for _ in range(number_of_orders)
    ]

    # Filtrar válidos y eliminar duplicados manteniendo orden
    valid_orders = []
    for item in orders:
        if item in product_list and item not in valid_orders:
            valid_orders.append(item)

    return valid_orders


def update_inventory(customer_orders, inventory):
    # 1. Restar 1 a los productos pedidos
    updated_quantities = {
        product: (quantity - 1 if product in customer_orders else quantity)
        for product, quantity in inventory.items()
    }

    # 2. Filtrar productos agotados
    cleaned_inventory = {
        product: quantity
        for product, quantity in updated_quantities.items()
        if quantity > 0
    }

    return cleaned_inventory



def print_updated_inventory(updated_inventory): # parametro de entrada diccionario
    print("\nUpdated Inventory:") # lo pongo para cumplir con el titulo
    for product, quantity in updated_inventory.items():
        print(f"{product}: {quantity}") # salida IMPRESION


def calculate_order_statistics(customer_orders, product_list): # parametros de entrada una lista y un diccionario
    total = len(customer_orders)
    percentage = (total / len(product_list)) * 100
    return total, percentage # devuelve un entero y un porcentaja para estadistica


def print_order_statistics(order_statistics):
    total, percentage = order_statistics
    print(f"Order Statistics: ")
    print(f"Total Products Ordered: {total}")
    print(f"Percentage of Unique Products Ordered: {percentage}")



def calculate_total_price(customer_orders):
    prices = {
        product: float(input(f"Enter the price of {product}: "))
        for product in customer_orders
    }

    total = sum(prices.values())

    return total


def print_total_price(total):
    print(f"Total Price: {total}")


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------

lista_productos = ['t-shirt', 'mug', 'hat', 'book', 'keychain']

inventory = initialize_inventory(lista_productos) # parametro es una lista
                                                  # devuelve un diccionario 

customer_orders = get_customer_orders(lista_productos) # parametro es una lista
                                                       # devuelve una lista 

order_statistics = calculate_order_statistics(customer_orders, lista_productos) # parametros entrada una lista y un diccionario,
                                                                                # devuelve un entero y un porcentaja para estadistica

print_order_statistics(order_statistics) # parametros entrada datos de estadistica
                                         # salida IMPRESION                                      

inventory = update_inventory(customer_orders, inventory) # parametro de entrada una lista y un diccionario
                                                         # devuelve un diccionario

print_updated_inventory(inventory) # parametro de entrada diccionario
                                   # salida IMPRESION

total = calculate_total_price(customer_orders) # parametro entrada lista
                                                                   # salida datos para estatidistica

print_total_price( total) # parametros entrada datos estadistica
                                             # salida IMPRESION

 
