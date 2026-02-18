#Name:Wendy Orina
#Date:17/02/2026
#Program to show lists in python
#List of friends
friends = ["Kelly","Sam","Tom","Praise"]

print(friends)
friends.sort()
print(friends)
friends.reverse()
print(friends)
friends.append("Kal")
print(friends)
new_friends = ["Obi","Elle","Dustin","Steve"]

print(len(new_friends))

#new list of students
students = friends + new_friends

print(students)
students.pop()
print(students)

students.insert(5,"Tin")
print(students)

students.insert(7,"Randy")
print(students)

students.remove("Obi")
print(students)

new_students = students.copy
print(new_students)