product = {
    "product_id": "p2001",
    "name": "Wireless Headphones",
    "price": 99.99,
    "stock": 45,
    "specs": {
        "brand": "Sony",
        "color": "Black",
        "wireless": True,
        "battery_life": "20 hours"
    },
    "reviews": [
        {"user": "Alice", "rating": 5, "comment": "Great sound quality!"},
        {"user": "Bob", "rating": 4, "comment": "Good battery life."}
    ]
}

ratings = [review['rating'] for review in product['reviews']]
print(ratings)

for spec, value in product['specs'].items():
    print(f"{spec.replace('_', ' ').title()}: {value}")

