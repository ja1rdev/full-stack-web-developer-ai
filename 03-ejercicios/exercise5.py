# A store offers 15% discount on the total purchase and a customer wants to know how much he will
# ultimately have to pay for his purchase

total = float(input("Enter your puchase total: "))

final_price = total - (total * 0.15)

print(f"The final price to pay is {final_price:.2f}")