from unittest import result


num = [1,2,3,4]
def addNum(num):
    return num+num

def tripple_num(num):
    return num*3

tripple_result = map(tripple_num,num)
print("tripple result ",list(tripple_result))

tripple_result2=map(lambda x: x + x, num)
print("result 2 ",list(tripple_result2))

result = map(addNum,num)
print("before" , result)
print("after",list(result))


result2=map(lambda x: x + x, num)
print("result 2 ",list(result2))

result3=map(lambda y: y*y, num)
print("result 3 ",list(result3))

num1 = [1,2,3,4]
num2 = [5,6,7,8]
num3 = [7,8,9,10]

result4 = map(lambda x ,y: x+y ,num1,num2)
print("result 4 ",list(result4))

trippleresult4 = map(lambda x ,y, z: x+y+z ,num1,num2,num3)
print("tripple result 4 ",list(trippleresult4))


result5 = map(lambda x,y,z,a,b,c : a+b-c*x/7**y+z , num1,num1,num1,num2,num2,num2) 
print("result 5 ",list(result5))




#######################  filter

ages = [23, 17, 21, 20, 19, 34, 40, 41, 22, 25, 27]

young_folks = filter(lambda person_age: person_age < 21,ages)
print(list(young_folks))


#named
def is_not_21(person_age):
    if person_age < 21:
        return True
    else:
        return False

young_people = list(filter(is_not_21,ages))
print(young_people)
