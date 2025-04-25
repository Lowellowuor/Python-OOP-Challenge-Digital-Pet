class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 3)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} enjoyed a tasty meal!")
        else:
            print(f"{self.name} is already full.")
        self.get_status()

    def sleep(self):
        if self.energy < 10:
            self.energy = min(10, self.energy + 5)
            print(f"{self.name} had a good nap and feels more rested.")
        else:
            print(f"{self.name} is not tired right now.")
        self.get_status()

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} had fun playing!")
        else:
            print(f"{self.name} is too tired to play.")
        self.get_status()

    def get_status(self):
        hunger_level = "full" if self.hunger == 0 else "slightly hungry" if self.hunger <= 3 else "hungry" if self.hunger <= 7 else "very hungry"
        energy_level = "fully rested" if self.energy == 10 else "energetic" if self.energy >= 7 else "a bit tired" if self.energy >= 3 else "tired"
        happiness_level = "very happy" if self.happiness >= 8 else "happy" if self.happiness >= 5 else "a bit sad" if self.happiness >= 2 else "sad"
        print(f"\n--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger} ({hunger_level})")
        print(f"Energy: {self.energy} ({energy_level})")
        print(f"Happiness: {self.happiness} ({happiness_level})")
        if self.tricks:
            print(f"Learned Tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
        print("-------------------------\n")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
            self.get_status()
        else:
            print(f"{self.name} already knows the trick: {trick}.")
            self.get_status()

    def show_tricks(self):
        if self.tricks:
            print(f"\n--- {self.name}'s Learned Tricks ---")
            for i, trick in enumerate(self.tricks):
                print(f"{i+1}. {trick}")
            print("-------------------------------\n")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")