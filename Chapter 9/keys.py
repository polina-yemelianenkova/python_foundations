customer = {
    "name": "Phillip",
    "customer_number": "C15464",
    "orders": [
        {
            "id": "1234",
            "items": ["TV", "PS5"],
            "total": 2003.99
        },
        {
            "id": "1645",
            "items": ["Switch2", "Mario Cart"],
            "total": 500.99
        }
    ]
}



for order in customer["orders"]:
    print(order)