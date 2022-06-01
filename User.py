# your improved User class goes here
class User:
    posts = [] #????????
    def __init__(self, name, email, license, age, gender):
        self.name = name
        self.email = email
        self.license = license
        self.age = age
        self.gender = gender
        
    def __str__(self):
        return f"My name is {self.name}. I am a {self.age} year old {self.gender} and my email address is {self.email}"

    def __post__(self):
        