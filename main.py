
from pet import Pet

if __name__ == "__main__":
    my_pet = Pet("Buddy")
    my_pet.get_status()

    my_pet.eat()
    my_pet.play()
    my_pet.sleep()

    my_pet.play()
    my_pet.eat()

    my_pet.train("Sit")
    my_pet.train("Fetch")
    my_pet.train("Roll Over")
    my_pet.train("Sit") # Try to teach a trick already learned

    my_pet.show_tricks()

    # Let's make Buddy very hungry and tired
    my_pet.play()
    my_pet.play()
    my_pet.play()
    my_pet.play()
    my_pet.play()

    my_pet.get_status()

    # Try to play when tired
    my_pet.play()

    # Let Buddy sleep to recover
    my_pet.sleep()
    my_pet.sleep()

    my_pet.get_status()