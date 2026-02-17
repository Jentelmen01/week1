class PetGuest:
    hotel_name = "Paws & Relax Hotel"
    total_guests = 0
    def __init__(self,pet_name,owner_id,toys=None):
        self.pet_name = pet_name
        self.owner_id = owner_id
        self.toys = []
        PetGuest.total_guests += 1
    def add_toy(self,toy_name):
        if toy_name:
            self.toys.append(toy_name)
            print(f"Added toy: {toy_name}")
    def remove_toy(self,toy_name):
        if toy_name in self.toys:
            self.toys.remove(toy_name)
            print(f"Removed toy: {toy_name}")
        else:
            print("Toy not found")
    def display_guest(self):
        print(f"Guest: {self.pet_name} (Owner: {self.owner_id})at {PetGuest.hotel_name}")


g1 = PetGuest("Mittens", "P-201")
g2 = PetGuest("Rex", "P-202")

g1.display_guest()
g1.add_toy("Ball")
g1.add_toy("Mouse")
g1.remove_toy("Mouse")

g2.display_guest()
g2.remove_toy("Bone")

print(f"Total guests: {PetGuest.total_guests}")