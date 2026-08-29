class Dog:
    breed = "Labrador" # attribute of the class
    age = 5
    color = "Brown"

    def bark(self): # method of the class
        return "Woof Woof"

    def eat(self):
        return "I am eating"

    def sleep(self):
        return "I am sleeping"

    def wag_tail(self):
        return "I am wagging my tail"
    
    def name_of_dog(self, name):
        self.name = name # attribute of the instance
        return f"My name is {self.name}" # return statement of the method

c1 = Dog() # instance of the class = object of the class
c1.name_of_dog("Buddy")
print(f"c1.breed: {c1.breed}")
print(f"c1.age: {c1.age}")
print(f"c1.color: {c1.color}")
print(f"c1.bark(): {c1.bark()}") # equivalent to Dog.bark(c1)
print(f"c1.eat(): {c1.eat()}")
print(f"c1.sleep(): {c1.sleep()}")
print(f"c1.wag_tail(): {c1.wag_tail()}")
print(f"c1.name: {c1.name}")

c2 = Dog()
c2.name_of_dog("Max")
print(f"c2.name: {c2.name}")

# Assignment:
# Create a class called Car with the following attributes: make, model, year
# Create a method called start_engine that returns "The engine is starting"
# Create a method called stop_engine that returns "The engine is stopping"
# Create a method called drive that returns "I am driving"
# Create a method called park that returns "I am parking"