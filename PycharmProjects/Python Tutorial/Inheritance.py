class Employee:
    raise_amt = 1.04
    def __init__(self,firstname,lastname,pay):
        self.firstname = firstname
        self.Lastname  =lastname
        self.pay = pay
    def PrintName(self):
        return '{} {} '.format(self.firstname , self.Lastname)
    def applyraise(self):
        self.pay = int(self.pay * self .raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self,firstname,lastname,pay,prog_lang):
        super().__init__(firstname,lastname,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,firstname,lastname,pay,employees=None):
        super().__init__(firstname,lastname,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.PrintName())


dev_1 = Developer('Priya','Joshi',72000,'Python')
dev_2 = Developer('Test','User',72000,'Java')

mgr_1 = Manager('sue','smith',90000,[dev_1])
print(mgr_1.PrintName())
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
print('---------------------------Removed---------------------------------------')
mgr_1.print_emps()

# print(dev_1.PrintName())
# print(dev_1.prog_lang)
