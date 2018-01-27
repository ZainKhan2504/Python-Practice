class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+" is now sitting")
    def roll_over(self):
        print(self.name.title()+" rolled over!")

namei =input("what is the name of your dog: ")
agei = input("what's "+namei+" age: ")
my_dog = Dog(namei,agei)
my_dog.sit()
my_dog.roll_over()