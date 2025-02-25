from abc import ABC, abstractmethod

class Pet(ABC):
    
    def __init__(self, hunger:int=50, happiness:int=50, energy:int=50, name:str=""):
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.name = name

    @property
    def hunger(self):
        return f"Hunger: {self.__hunger}"
    
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
        return f"Happiness: {self.__happiness}"
    
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
        return f"Energy: {self.__energy}"
    
    @happiness.setter
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
        self.hunger = self.__hunger - 20
        self.energy = self.__energy + 10
    
    def play(self):
        self.happiness = self.__happiness + 15
        self.energy = self.__energy - 10

    def sleep(self):
        self.energy = self.__energy + 20
        self.hunger = self.__hunger + 10

    def show_status(self):
        return f"Hunger: {self.hunger}\nHappiness: {self.happiness}\nEnergy: {self.energy}"
    
    def random_event(self):
        pass

    @abstractmethod
    def special_ability(self):
        pass

class Dog(Pet):
    
    def __init__(self, hunger:50, happiness:50, energy:50, name:str):
        super().__init__(hunger, happiness, energy, name)
    
    def play(self):
        self.happiness + 20

    def special_ability(self, happiness):
        if self.happiness >= 80:
            return print("\nLoyal Companion: Hunger decreases by 10 because your pet is too excited and forgets to eat.")
        else:
            print("Pets happiness level must be >= 80.")
        


    
def main():
    while True:
        userin = input("enter a name\n")

        pet = Dog(userin)

        pet.name


if __name__ == "__main__":
    main()

