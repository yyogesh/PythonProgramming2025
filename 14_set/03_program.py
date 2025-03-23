# List: Used for ordered collection of order records
# Each order contains: order_id, customer_id, products, order_date, total_amount
orders = [
        (1001, "C789", ["laptop", "mouse", "keyboard"], "2025-01-15", 1299.99),
        (1002, "C456", ["monitor", "webcam"], "2025-01-16", 349.98),
        (1003, "C123", ["laptop", "laptop_stand", "mouse"], "2025-01-18", 1199.97),
        (1004, "C789", ["external_drive", "webcam"], "2025-02-02", 159.98),
        (1005, "C456", ["keyboard", "mouse"], "2025-02-10", 89.99),
        (1006, "C123", ["monitor", "webcam", "keyboard"], "2025-02-15", 429.97),
        (1007, "C789", ["laptop_stand", "external_drive"], "2025-03-01", 109.98)
    ]

# Each tuple contains: customer_id, name, tier, join_date
customers = [
        ("C123", "Alex Johnson", "Gold", "2023-05-10"),
        ("C456", "Taylor Smith", "Silver", "2024-03-22"),
        ("C789", "Jordan Lee", "Gold", "2023-11-05")
    ]

# Set: Used for unique collection of products for inventory tracking
inventory = {
        "laptop", "monitor", "keyboard", "mouse", "webcam", 
        "external_drive", "laptop_stand", "headphones", "printer"
    }


ordered_products = set()
# (1001, "C789", ["laptop", "mouse", "keyboard"], "2025-01-15", 1299.99)
for order in orders:
    for product in order[2]:
        ordered_products.add(product)

print(ordered_products)
not_ordered = inventory.difference(ordered_products)
print(not_ordered)

all_products = []
for order in orders:
    all_products.extend(order[2])

print(all_products)