import datetime
class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
        self._age = None
        self._age_last_calculated = None
        self.recalculate_age()
    def recalculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year,self.birthdate.month,self.birthdate.day):
            age -= 1

        self.age = age
        self.age_last_calculated = today
    def age(self):
        if(datetime.date.today() > self._age_last_calculated):
            self.recalculate_age()

        return self._age
    def __str__(self):
        return "string"
person = Person(
            "Jane",
            datetime.date(1990,7,26)
        )
print(person.__str__())
print(person.name)
print(person.age)