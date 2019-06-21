from Calculator import test
import sys
import os
class Anyclass:
    '''This is an anyclass.'''
    def __int__(self,*Args):
        for args in Args:
            return "%s".join(args)
#     def __init__(self,**kwargs):
#         for k,v in kwargs.items():
#             setattr(self,k,v)
#     def __str__(self):
#         attrs = ["%s=%s" % (k,v) for (k,v) in self.__dict__.items()]
#         classname = self.__class__.__name__
#         return "%s %s" %(classname,",".join(attrs))
#
#
# args = {"1":"Priya","2":"Tai","3":"AAi"}
# print(Anyclass(**args))
args = ("Priya","Tai","Aai")
print(args)
print(test)
#print(sys.path)
print(os.__file__)