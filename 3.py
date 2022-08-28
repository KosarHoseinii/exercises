class Cat():
    def __init__(self, race, skin_color, eye_color, Weight):
        self.race = race
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.weight = Weight



class Bird():
    def __init__(self, type, skin_color, eye_color, Weight):
        self.type = type
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.weight = Weight



c1=Cat("Ragdale", "white", "blue", "7 kg") 
c2=Cat("Siamese", "brown","black", "5 kg")   

b1=Bird("parrot", "green", "black", "63 g")
b2=Bird("Peacock", "blue", "brown", "6 kg")


print("The first type of cat:")
print(f"race: {c1.race}")
print(f"skin color: {c1.skin_color}")
print(f"eye color: {c1.eye_color}")
print(f"weight: {c1.weight}")

print("____________________")

print("The second type of cat:")

print(f"race: {c2.race}")
print(f"skin color: {c2.skin_color}")
print(f"eye color: {c2.eye_color}")
print(f"weight: {c2.weight}")
print("____________________")

print("The first type of bird:")

print(f"type: {b1.type}")
print(f"skin color: {b1.skin_color}")
print(f"eye color: {b1.eye_color}")
print(f"weight: {b1.weight}")

print("____________________")

print("The second type of bird:")
print(f"type: {b2.type}")
print(f"skin color: {b2.skin_color}")
print(f"eye color: {b2.eye_color}")
print(f"weight: {b2.weight}")
