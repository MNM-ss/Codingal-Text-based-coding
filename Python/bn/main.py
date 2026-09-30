class FamilyMember:
    def show_traits(self):
        print("Eye color: ", self.eye_color)
        print("Height:", self.height, "cm")

class Kid(FamilyMember):
    def __init__(self, name, age, eye_color, height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm)

    def show_traits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_traits()

    def favourite_hobby(self, hobby):
        print(self.name, "loves", hobby)

child = Kid("Alice", 10, "blue", 140)
child.show_traits()
child.favourite_hobby("painting and reading")

print("Is Kid a subclass of FamilyMember?", issubclass(Kid, FamilyMember))
