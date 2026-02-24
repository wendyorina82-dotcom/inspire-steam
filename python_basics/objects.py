#Name:Wendy Orina
#Date:19/02/2026
#Program to show objects

class Human:
    #First we define the attributes of human beings
    type = "Mammal"
    legs = 2
    brain = True
    Warm_blooded = True
    city = "Kisumu"

    #We then create a constructor for the class object
    #The constructor will be used to create copies of this objects
    def __init__(self,name,age):
        self.human_name = name
        self.human_age = age
    def tell_story(self):
        print(f"Hello I am {self.human_name} Here is the story")    
        print("Jeffery Dahmer is a serial killer")
#Create the objects
Orina = Human("Orina",19)
Tin = Human("Tin",23)

#Let the humans created do things
Orina.tell_story()
print("Orina's age is" , Orina.human_age)

#Modify one of the objects without modifying other objects
Tin.city = "Nairobi"

print("Tin's location is:",Tin.city)
print("Orina's locations is:",Orina.city)