# Abstraction
# Encapsulation
# Polymorphism--> multiple forms
# Inheritence-->classes and objects


# Encapsulation
student1={
    "name":"Tanmay",
    "marks":100
}
student2={
    "name":"Shagun",
    "marks":90
}


# class-->classes are callable
class person:
    pass
p = person()
print(p)


hex(id(p))


# class with a method

class person:
    name="Tanmay"

    def say_hi(self):
        print(f"Hello everyone ! I am {self.name}")
p=person()

p.say_hi()
person.say_hi(p)