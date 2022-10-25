#object oriented programming
#Real world objects: Are made up of Attributes and Capabilities
#Dog Attributes in tech it is called field or variable
#Dog capabilities in tech it is called method or function

#creating a DOG Object

class Dog:,
    def __init__(self, name="", height="0", weight="0" ): #self allows a object to refer to itself just as you will refer to yourself as 'my'
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))

def main():
    spot = Dog("Spot")
    spot.bark()
    bowser = Dog()
    bowser.bark()

main()

#second one

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1

    def die(self):
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1.o

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))
