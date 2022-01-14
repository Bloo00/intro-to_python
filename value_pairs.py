object1 = {"name": 'One', "location": 'Remote', "age": 1}
object2 = {"name": 'Two', "location": 'San Francisco'}


def value_pair(obj1,obj2,key):
    result = []

    result.append(obj1.get(key))
    result.append(obj2.get(key))
    return result

print(value_pair(object1,object2,"name"))