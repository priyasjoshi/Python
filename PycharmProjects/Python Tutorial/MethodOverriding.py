class Father:
    def print_firstname(self):
        print("Father_name")
    def print_lastname(self):
        print("Surname")

class Son(Father):
    def print_firstname(self):
        print("Son_name")

Obj_Son = Son()
Obj_Son.print_firstname()
Obj_Son.print_lastname()