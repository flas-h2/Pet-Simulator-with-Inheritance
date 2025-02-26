from abc import ABC, abstractmethod

class Pet(ABC):
    
    def __init__(self, hunger:int=50, happiness:int=50, energy:int=50, name:str=""):
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
    def __init__(self, name: str, hunger: int = 50, happiness: int = 50, energy: int = 50):
        super().__init__(hunger, happiness, energy, name)
    
    def play(self):
        self.happiness = self.__happiness + 20

    def special_ability(self):
        if self.happiness >= 80:
            self.hunger -= 10
            print("\nLoyal Companion: Hunger decreases by 10 because your pet is too excited and forgets to eat.")
        else:
            print("Pet's happiness level must be >= 80.")
        


    
def main():
    userin = input("Enter a name for your pet: ")
    pet = Dog(name=userin)

    while True:
        print("\nPet Status:")
        print(pet.show_status())
        
        print("\nOptions: [1] Feed [2] Play [3] Sleep [4] Use Special Ability [5] Exit")
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

