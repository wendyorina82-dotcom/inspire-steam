#Name:Wendy Orina
#Date:12/02/2026
#String formatting

#Get string length
sentence="I watch anime"
string_length=len(sentence)

print(f"The length is:{string_length}")

#Spliting a string
sentence_2="Mathematics Physics"
split=sentence_2.split(" ")

print(f"the first subject is: {split[0]}")

#Make everything CAPS
mpesa_code = "ud23vsgedh"

capitalized = mpesa_code.upper()
print(f"New mpesa code:{capitalized}")

#Make everything in lower case
mpesa_code = "UD67HJIWHY"

small = mpesa_code.lower()
print(f"New mpesa code:{small}")

#Replacing characters in string

balance = "200Kes"
amount_added = "50Kes"

cleaned_balance = balance.replace("Kes","")
print(f"cleaned_balance:{cleaned_balance}")

cleaned_amount_added = amount_added.replace("Kes", "")
print(f"cleaned amount added:{cleaned_amount_added}")

#New balance
new_balance = int(cleaned_balance) + int(cleaned_amount_added)

print(f"New balance:{new_balance}")


