#Name:Wendy Orina
#Date:17/02/2026
#Program to formath the output in different ways

name = "Wendy Orina" #Name

weight = 56 #weight in kgs

fav_team = "Manchester United"

height = 1.67 #height in cms

#1 Format using printf(f"{}"")

print(f"My name is {name} and I weigh {weight} kgs")

# 2 Using f string
msg = f"My name is{name} and I support {fav_team}"
print(msg)

#3 Using {} and .format ()

print("My name is {0} and I am {1} cms tall".format (name,height))

#4 Using output specifiers %s -strings 

print("I support %s " % fav_team)