# phonebook = {}
# phonebook["Priya"] = 123456789
# phonebook["Tejas"] = 123456780
# print(phonebook)

phonebook = {"Priya": 123456789,
             "Tejas" : 123456780,
             "Jill" : 1265656256
}

del phonebook["Priya"]
print(phonebook)
print('TEJAS' in phonebook)
# for name,number in phonebook.items():
#     if name == "Priya":
#         print(name,number)
#
#     else:
#         print(phonebook)
#
AddressBook =  dict([('Priya',4139),('guido',4127),('Jack',4585)])
print(AddressBook)

# for i,v in enumerate(['tic','toc','toe']):
#     print(i,v)

basket = ['apple','orange','apple','pear','banana']
for f in sorted(set(basket)):
    print(f)


