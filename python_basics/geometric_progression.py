#Name:Wendy Orina
#Date:02/11/2026
#Program to calculate geometric progression


a = int(input("Enter first term"))
r = int(input("Enter the common ratio"))
n = int(input("Enter the number of terms"))

nth_term = a * (r ** (n - 1))
Sn = a * (r**n - 1) / (r - 1)
print(f"The nth term is: {nth_term}")
print(f"The sum of terms is: {Sn}")

