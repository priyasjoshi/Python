class Employee:
    num_of_emps = 0
    raise_amt = 1.05
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps +=1

    def email(self):
        return '{1}_{0}@company.com'.format(self.first,self.last)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


Employee.set_raise_amt(1.06)
print(Employee.raise_amt)

import datetime
my_date = datetime.date(2018,2,4)
print(Employee.is_workday(my_date))