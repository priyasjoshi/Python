lis = ['5','4','2','1']
newlis = set(map(int,lis))
newlis.add(6)
newlis.add((6,5))
newlis.remove(6)
print(newlis)