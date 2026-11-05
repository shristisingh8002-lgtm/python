class person:
    
    def __init__(self, name, occupation):
        print("hey i am a person")
        self.name = name
        self.occupation = occupation

def info(self):
    print(f"{self.name} is a {self.occupation}")

a = person("harry", "developer")
b = person("divya", "HR")

# a.name = "divya"
# a.occupation = "HR"
# a.info()
