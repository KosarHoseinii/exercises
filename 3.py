class Animal():
    def __init__(self,name,type,number_of_children,eye_color):
        self.animals_name= name
        self.animals_type= type
        self.animals_number_of_children= number_of_children
        self.animals_eye_color= eye_color

    
a1=Animal("cat","mammal",3,"green")
a2=Animal("bird","laying eggs",5,"brown")

print("The first animal:")
print("Animal name:  ",a1.animals_name)
print("Type of animal:  ",a1.animals_type)
print("Average number of children:  ",a1.animals_number_of_children)
print("The color of the animal's eyes:  ",a1.animals_eye_color)

print("The second animal:")
print("Animal name:  ",a2.animals_name)
print("Type of animal:  ",a2.animals_type)
print("Average number of children:  ",a2.animals_number_of_children)
print("The color of the animal's eyes:  ",a2.animals_eye_color)