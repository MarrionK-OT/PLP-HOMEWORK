def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price

original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

result = calculate_discount(original_price, discount_percentage)
print(f"Final price: Ksh{result:.2f}")