#Name:Wendy Orina
#Date:23/02/2026
#Program to show inheritance in python

class Animal():

    def__init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weight {weight}")

    def eat(self,food):
        print(f"The animal eats {food}")    


class dog(Animal):

    def__init__(self,species,weight,food):
        super().__init__(species,weight,food)
        self.color = color
        self.breed = breed
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weight {weight}")
        
    def eat(self,food):
        print(f"The animal eats {food}") 
    def barks(self):
        print("The dog says woof woof")    

 
class Horse(Animal):

    def__init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weight {weight}")
        
    def neighs(self):
        print(f"The animal says neigh neigh)        