
ppl = [
  {'name': 'Khalid Robinson', 'age': 22},
  {'name': 'Ariel Winter', 'age': 20},
  {'name': 'Post Malone', 'age': 25},
  {"name": 'Willow Smith', 'age': 17}
]


def adults(ppl):
    result =[]
    for person in ppl:
        if(person.get("age") >= 18):
            result.append(person.get("name"))


    return result


print(adults(ppl))