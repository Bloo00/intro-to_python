from __future__ import print_function


object1 = {"name": 'One', "location": 'Remote', "age": 1}
object = {"name": 'Two', "location": 'San Francisco'}


def value_pair(obj,key):
    result = []

    if key in obj.keys():
        print("key exsits")
    else:
        print("no key")

    

value_pair(object,"name")