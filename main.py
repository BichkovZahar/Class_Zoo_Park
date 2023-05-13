import random

class Animal:
    def __init__(self, species, name, age , health = random.randint(1 , 100), hunger = random.randint(1 , 70), happiness  =  random.randint(1 , 80)):
        self.species = species
        self.name = name
        self.age = age
        self.health = health
        self.hunger = hunger
        self.happiness = happiness

    def grow(self):
        self.age += 1
        self.health += random.randint(0, 30)
        self.hunger -= random.randint(0, 30)
        self.happiness -= random.randint(0, 30)

    def eat(self):
        self.hunger += random.randint(0, 50)
        self.health += random.randint(0, 40)

    def play(self):
        self.happiness += random.randint(0, 30)
        self.hunger -= random.randint(0 , 20)


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        return f'{self.animals} rr {self.name}'

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def feed_all(self):
        for animal in self.animals:
            animal.eat()

    def play_with(self):
        for animal in self.animals:
            animal.play()

    def grow_all(self):
        for animal in self.animals:
            animal.grow()

    def __str__(self):
        return f"Zoo: {self.name} " \
               f"\nAnimals: {' , '.join([animal.name for animal in self.animals])}."


def save_state_to_file(zoo, day):
    with open(f"Day_{day}.txt", "w") as file:
        file.write(str(zoo))
        for animal in zoo.animals:
            file.write(f"\nSpecies -> {animal.species} | Name -> {animal.name} | Age -> {animal.age} | Health -> {animal.health} "
                       f"| Hunger -> {animal.hunger} | Happiness ->  {animal.happiness}")




name_zoo = Zoo("Victoria")

animal1 = Animal("Lion", "Richard" , 1)
name_zoo.add_animal(animal1)

animal2 = Animal("Mavka", "Naruto" , 4)
name_zoo.add_animal(animal2)

animal3 = Animal("Induk", "Sakura" , 2)
name_zoo.add_animal(animal3)

for day in range(1, 11):
    name_zoo.feed_all()
    name_zoo.play_with()
    name_zoo.grow_all()
    save_state_to_file(name_zoo, day)
