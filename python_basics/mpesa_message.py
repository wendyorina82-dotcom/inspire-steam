#Name:Wendy Orina
#Date:12/02/2026
#Mpesa message

From = "Wendy Orina"
amount_added = 600
mpesa_balance = 1500
mpesa_code = "QGHU126HUF"


print("CONFIRMED")
print(f"You have received {amount_added}KES from {From}")
print(f"mpesa_code:{mpesa_code}")

#New balance
new_balance= int(amount_added) + int(mpesa_balance)

print(f"Your new balance is {new_balance}KES")

