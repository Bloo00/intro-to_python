from unittest import result


def my_first_function(x,y,name="kabin"):
    for i in range(x):
        for j in range (y):
            print ("y", name)
            
    print("x")

students = [
    { 
        "name": "Kimmie",
        "city": "Atlanta"
    },
    { 
        "name": "Chris",
        "city": "Salt Lake City"
    },
    { 
        "name": "Zack",
        "city": "Los Angeles"
    },
     { 
        "name": "John",
        "city": "Atlanta"
    },
    { 
        "name": "Jane",
        "city": "New York"
    },
    { 
        "name": "Rob",
        "city": "Los Angeles"
    },
     { 
        "name": "Harper",
        "city": "Washington"
    },
    { 
        "name": "Mike",
        "city": "Seattle"
    },
    { 
        "name": "Set",
        "city": "San Francisco"
    },
]

my_first_function(4,4)


def get_names(students):
    result = []
    for name in students:
        result.append(name.get('name'))
    return result

print("Name List: ", get_names(students))
    

def parse_by_cities(students):
    result_dict = {}
    temp_list=[]
    for student in students:
        if student.get('city'):
            if result_dict.get(student.get('city')):
                print('this exists')
                city_list = result_dict[student.get('city')]
                city_list.append(student.get('name'))
            else:
                print("no exist")
                result_dict[student.get('city')] = []
                city_list = result_dict[student.get('city')]
                city_list.append(student.get('name'))

    return result_dict

print(parse_by_cities(students))