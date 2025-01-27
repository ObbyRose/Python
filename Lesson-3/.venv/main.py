class Person: 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print(f"{self.first_name} says hello!")

person_1 = Person(last_name="Doe", first_name="John")
person_1.greet()

class SuperHero:
    def __init__( self, name, alias, power, strength_level, team: str = None , is_active: bool = True):
        self.name = name
        self.alias = alias
        self.power = power
        self.strength_level = strength_level
        self.team = team
        self.is_active = is_active

    def introduce(self):
        print(f"I am {self.alias}, also known as {self.name}. My power is {self.power}, and I fight for {self.team}!")

    def train(self, hours):
        self.strength_level += hours * 10
        print(f"after training for {hours} your strength level is now {self.strength_level}")

    def fight_villian(self, villian_name):
        print(f"{self.alias} is fighting {villian_name}")
        self.strength_level -= 5
        if self.strength_level < 10:
            print(f"{self.alias} is too weak to fight {villian_name}")
            self.is_active = False

    def retire(self):
        self.is_active = False
        print(f"{self.alias} is retired from the hero duties")

    def reactivate(self):
        self.is_active = True
        print(f"{self.alias} is back in action!")

hero_1 = SuperHero(name="Peter Parker", alias="Spider-Man", power="Spider-Sense", strength_level=50, team="Avengers")
hero_2 = SuperHero(name="Tony Stark", alias="Iron Man", power="Genius Intellect", strength_level=70, team="Avengers")

hero_1.introduce()
hero_2.introduce()

hero_1.train(5)
hero_2.train(3)

hero_1.fight_villian("Green Goblin")
hero_2.fight_villian("Thanos")

hero_1.retire()
hero_2.retire()

hero_1.reactivate()
hero_2.reactivate()

class BankAccount: 
    def __init__(self, account_holder, balance = float):
        self.account_holder = account_holder
        self.balance = balance

    def deposist(self , amount):
        self.balance += amount
        print(f"Your new balance is {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Your new balance is {self.balance}")
    
    def check_balance(self):
        print(f"Your current balance is {self.balance}")

user_1 = BankAccount(account_holder="John Doe", balance=1000.97)

user_1.deposist(500)

user_1.withdraw(200)

user_1.check_balance()


class Book:
    def __init__(self, title, author, number_of_copies: int):
        self.title = title
        self.author = author
        self.number_of_copies = number_of_copies

    def display_info(self):
        print(f"{self.title} by {self.author} has {self.number_of_copies} copies left")
    
    def borrow(self):
        self.number_of_copies -= 1
        print(f"you have borrowed {self.title} by {self.author} and now there are {self.number_of_copies} copies left")

    def return_book(self):
        self.number_of_copies += 1
        print(f"you have returned {self.title} by {self.author} and now there are {self.number_of_copies} copies left") 

book_1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", number_of_copies=5)

book_1.display_info()

book_1.borrow()

book_1.return_book()


class Stundent:
    def __init__(self, name, grades = []):
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"you have added {grade} to {self.name}'s grades")

    def avg_grade(self):
        avg = sum(self.grades) / len(self.grades)
        print(f"{self.name}'s average grade is {avg}")

student_1 = Stundent(name="John Doe", grades=[90, 85, 95, 100])

student_1.add_grade(50)
student_1.avg_grade()