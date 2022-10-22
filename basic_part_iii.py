#class
class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    #method
    def greeting(self):
        print("Hello, my name is", self.name)
user_1 = User("Elian Muñoz", 21, "Valle del limari 096")
user_2 = User("Ximena Santana", 22, "Avenida siempre viva")
print(user_1.name, user_1.age, user_1.address)
print(user_2.name, user_2.age, user_2.address)
user_1.greeting()
user_2.greeting()

#Self, delete properties and objects
user_1.name = 'Joseph' #modify 
user_1.greeting()
# del user_1.name #delete property
# user_1.greeting()

#Inheritance (use the same methods and properties than User)
class Admin(User):
    def superGreeting(self):
        print("Hello, my name is", self.name, 'and im ADMIN')
admin = Admin('Joseph', 28, 'Avenue 17')
admin.superGreeting()

#example
class Team:
    def __init__(self, name):
        self.name = name
    def desc(self):
        print("The league of",self.name,"is",self.league)
class PremierLeague(Team):
    league = "Premier League"
class LaLiga(Team):
    league = "LaLiga"
class Bundesliga(Team):
    league = "Bundesliga"
team = PremierLeague("Manchester City")
team_2 = LaLiga("Real Madrid")
team_3 = Bundesliga("Bayern Munich")
team.desc()
team_2.desc()
team_3.desc()

