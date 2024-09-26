class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name,pet_type,owner=None) -> None:
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type {pet_type}. Must be one of {Pet.PET_TYPES}")
        self.name = name
        self.pet_type =pet_type
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self,name) -> None:
        self.name = name
        
    def pets(self):
        return Pet.all
    def add_pet(self,pet):
        if not isinstance(pet, Pet):
            raise TypeError("The provided pet is not of type Pet")
        if pet.owner is None:
            pet.owner =self
        else:
            raise ValueError("This pet already has an owner")
        
    def get_sorted_pets(self):
        owned_pets = [pet for pet in Pet.all if pet.owner == self]
        sorted_pets = sorted(owned_pets, key = lambda pet:pet.name)
        return sorted_pets