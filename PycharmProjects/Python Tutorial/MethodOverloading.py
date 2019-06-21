class Operations:
    def add (self, *args):
        result = 0
        for i in args:
            result += i
        return result

obj_1 = Operations()

print(obj_1.add(3,1,4,45))
