class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi , Iam {self.name} ")


person = Person("Arfan")
#print(person.name)
person.talk()

person2 = Person("Ashfaque")
person2.talk()
