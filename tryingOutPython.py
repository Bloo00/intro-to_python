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
    }
]

my_first_function(4,4)


def get_names(students):
    result = []
    for name in students:
        result.append(name.get('name'))
    return result

print("Name List: ", get_names(students))
    