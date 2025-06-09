serviceable_location = input("Is your location serviceable? (True/False): ").lower() == "true"
order_amount = float(input("Enter your order amount: ₹"))
minimum_order_amount = float(input("Enter the minimum amount: ₹"))
if serviceable_location and order_amount >= minimum_order_amount:
    print("Your order will be delivered.")
else:
    print("Delivery is not available for your order.")
