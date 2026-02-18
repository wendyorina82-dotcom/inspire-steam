#Name:Wendy Orina
#Date:17/02/2026
#Program to perform arithmetic operations

f_number = 12
s_number = 23
sum_number = f_number + s_number
diff_number = f_number - s_number
product_number = f_number * s_number
quotient_number = f_number / s_number

print("The sum of numbers %d "%sum_number)
print("The quotient of numbers %0.2f "%quotient_number)

#modulus - remainder
print(7%5)

#even and odd numbers
for x in range(0,21):
    if(x%2==1):
        print(f"{x} is odd number")
    elif(x%2==0):
        print(f"{x} is an even number")
    print(x)