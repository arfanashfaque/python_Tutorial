class Mammal():
    def walk(self):
        print("Walk")


class Dog(Mammal):   # this Dog(mammal) is where we called inheritance . ie mammal is parent class and dog is child class
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def meow(self):
        pass    #put pass, means the method cannot end with a def statement, something need to be inside that. so put pass


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.meow()
cat1.walk()

