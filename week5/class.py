# Parent class
class Person:
    def __init__(self, name, age, city):
        self.name = name        # public attribute
        self.__age = age        # private attribute (encapsulation)
        self.city = city

    # Getter for private attribute
    def get_age(self):
        return self.__age

    # Method
    def introduce(self):
        return f"My name is {self.name}, and I live in {self.city}."


# Child class inheriting from Person
class Doctor(Person):
    def __init__(self, name, age, city, specialization):
        super().__init__(name, age, city)   # call parent constructor
        self.specialization = specialization

    # Override method
    def introduce(self):
        return f"Dr. {self.name}, a {self.specialization} specialist, is practicing in {self.city}."


# Create objects
person1 = Person("Qufa", 40, "Addis Ababa")
doctor1 = Doctor("Qufa", 40, "Addis Ababa", "Cardiologist")

# Test
print(person1.introduce())  # My name is Qufa, and I live in Addis Ababa.
print(doctor1.introduce())  # Dr. Qufa, a Cardiologist specialist, is practicing in Addis Ababa.
print(doctor1.get_age())      # 40 (accessing private attribute via getter)
