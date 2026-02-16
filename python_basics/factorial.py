#Name:Wendy Orina
#Date:16/02/2026
#Program to calculate the factorials of a number

number =int(input("Enter the number x:"))
factorial = 1 #Initialized factorial on 1
for x in range(1,number+1):
    factorial *=x
number = number - 1
    print(f"{number}!={factorial}")