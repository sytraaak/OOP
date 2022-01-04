class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return str(f"{self.name} ({self.age} let)")

    def aging(self):
        self.age += 1

class Person:
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog

dog = Dog("Josifek", 8)
print(dog)
rudolf = Person("Rudolf Jelínek", dog)
karel = Person("Karel Jelínek", dog)
print(f"Rudolfův pes: {rudolf.dog}")
print(f"Karlův pes: {rudolf.dog}")
for _ in range(4):
    dog.aging()

print(f"Rudolfův pes: {rudolf.dog}")
print(f"Karlův pes: {rudolf.dog}")

