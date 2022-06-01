# your improved User class goes here
class User:
    all_posts = []
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.message = message
        
    def __str__(self):
        return f"My name is {self.name}. I am a {self.age} year old {self.gender} and my email address is {self.email}"

    def post(self, message):
        new_post = {'name': self.name, 'message': message}
        User.all_posts.append(new_post)

#########  Driver code ############

alice = User('Alice', '22', 'female')
bob = User('Bob', '57', 'male')
alice_post = alice.post('This is a test')
bob_post = bob.post('This is my test')
alice_post = alice.post('Did this work?')

print(User.all_posts)     