class Person:
    name = "harry"
    occupation = "software"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation} and has a net worth of {self.networth}")

a = Person()
a.name = "shubham"
a.occupation = "accountant"

b = Person()
b.name = "ritika"
b.occupation = "HR"
b.networth = 15
# print(a.name, a.occupation)
a.info()
b.info()