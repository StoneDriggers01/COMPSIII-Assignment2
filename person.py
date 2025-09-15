class Person:
    pass
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
    
    def __str__(self):
        return f"{self.name} is {self.age} years old and is from {self.country}."

    
Per_1 = Person('John', 17, 'Canada')
Per_2 = Person('Maria', 25, 'Spain')

print(Per_1)
print(Per_2)

