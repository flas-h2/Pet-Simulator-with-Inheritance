from abc import ABC, abstractmethod
import random
import time

class Pet(ABC):
    
    def __init__(self, name:str, hunger:int=50, happiness:int=50, energy:int=50):
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.name = name

    @property
    def hunger(self):
        return self.__hunger
    
    @hunger.setter
    def hunger(self, hunger):
        if hunger > 100:
            print("Cannot go above 100.")
            self.__hunger = 100
        elif hunger < 0:
            print("Cannot go below 0.")
            self.__hunger = 0
        else:
            self.__hunger = hunger

    @property
    def happiness(self):
        return self.__happiness
    
    @happiness.setter
    def happiness(self, happiness):
        if happiness > 100:
             print("Cannot go above 100.")
             self.__happiness = 100
        elif happiness < 0:
            print("Cannot go below 0.")
            self.__happiness = 0
        else:
            self.__happiness = happiness

    @property
    def energy(self):
        return self.__energy
    
    @energy.setter
    def energy(self, energy):
        if energy > 100:
            print("Cannot go above 100.")
            self.__energy = 100
        elif energy < 0:
            print("Cannot go below 0.")
            self.__energy = 0
        else:
            self.__energy = energy

    def feed(self):
        self.__hunger -= 20
        self.__energy += 10
    
    def play(self):
        self.__happiness += 15
        self.__energy -= 10

    def sleep(self):
        self.__energy += 20
        self.__hunger += 10

    def show_status(self):
        return f"Hunger: {self.hunger}\nHappiness: {self.happiness}\nEnergy: {self.energy}"
    
    def random_event(self):
        random_num = random.randrange(10)
        if random_num > -1 and random_num < 4:
            prob_rand_num = random.randrange(4)
            if prob_rand_num == 0:
                print(f"Random Event: {self.name} found a toy! Happiness increases by 15.")
                self.__happiness += 10
            elif prob_rand_num == 1:
                print(f"Random Event: {self.name} found a snack! Hunger decreased by 10.")
                self.__hunger -= 10
            elif prob_rand_num == 2:
                print(f"Random Event: {self.name} plays alone. Happiness increases by 10.")
                self.__happiness += 10
            else:
                print(f"Random Event: {self.name} has a bad dream. Energy decreases by 10.")
                self.__energy -= 10


    @abstractmethod
    def special_ability(self):
        pass

class Dog(Pet):
    def __init__(self, name: str, hunger: int = 50, happiness: int = 50, energy: int = 50):
        super().__init__(hunger, happiness, energy, name)
    
    def play(self):
        self.__happiness += 20

    
    def special_ability(self):
        if self.__happiness >= 80:
            self.__hunger -= 10
            print("\nLoyal Companion: Hunger decreases by 10 because your pet is too excited and forgets to eat.")
        else:
            print("Pet's happiness level must be >= 80.")
        
class Cat(Pet):
    def __init__(self, name: str, hunger: int = 50, happiness: int = 50, energy: int = 50):
        super().__init__(hunger, happiness, energy, name)

    def sleep(self):
        self.__energy += 30
        self.__hunger += 5

    def special_ability(self):
        if self.__energy <= 20:
            self.__energy += 15
            print("\nIndependent Napper: Your pet took a nap on its own and energy increased by 15!")
        else:
            print("Pet's energy level must be <= 20.")

class Dragon(Pet):
    def __init__(self, name: str, hunger: int = 50, happiness: int = 50, energy: int = 50):
        super().__init__(hunger, happiness, energy, name)
    
    def feed(self):
        self.__hunger -= 30
        self.__energy += 15
        self.__happiness += 10

    def play(self):
        self.__happiness += 25
        self.__hunger += 10
        self.__energy -= 5

    def special_ability(self):
        if self.energy <= 20:
            self.energy += 15
            print("\nIndependent Napper: Your pet took a nap on its own and energy increased by 15!")
        else:
            print("Pet's energy level must be <= 20.")


    
def main():
    userin = str(input("Enter a name for your pet: "))
    print('Choose a pet type:\n1. Dog\n2. Cat\n3. Dragon')
    while True:
        pet = input("Enter your choice (1/2/3): ")
        if pet == "1":
            pet = Dog(name=userin)
            break
        elif pet == "2":
            pet == Cat(name=userin)
            break
        elif pet == "3":
            pet == Dragon(name=userin)
            break
        else:
            print("Invalid Option, please try again!")

    while True:
        print("\nPet Status:")
        print(pet.show_status())
        
        print("\nOptions:\n[1] Feed\n[2] Play\n[3] Sleep\n[4] Use Special Ability\n[5] Exit")
        choice = input("Choose an action: ")

        if choice == "1":
            pet.feed()
            print(f"{pet.name} has been fed!")
        elif choice == "2":
            pet.play()
            print(f"{pet.name} played and is happier!")
        elif choice == "3":
            pet.sleep()
            print(f"{pet.name} slept and restored energy!")
        elif choice == "4":
            pet.special_ability()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")



if __name__ == "__main__":
    main()

