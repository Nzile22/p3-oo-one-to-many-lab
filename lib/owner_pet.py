class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all instances of Pet

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)  # Add this instance to the all list

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Private list to store pets

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        pet.owner = self  # Set the owner of the pet
        self._pets.append(pet)  # Add the pet to the owner's list

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

# Example usage:
try:
    owner1 = Owner("Alice")
    pet1 = Pet("Buddy", "dog", owner1)
    owner1.add_pet(pet1)

    pet2 = Pet("Whiskers", "cat")
    owner1.add_pet(pet2)  # This will raise an exception because pet2 has no owner set

except Exception as e:
    print(e)

# Adding pet2 to owner1
pet2.owner = owner1
owner1.add_pet(pet2)

# Getting sorted pets
sorted_pets = owner1.get_sorted_pets()
for pet in sorted_pets:
    print(f"{pet.name} the {pet.pet_type}")