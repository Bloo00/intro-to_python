from unittest import result


peeps = [
  {'name': "Pete", 'score': 2},
  {'name': "Dexter", 'score': 2},
  {'name': "Mike", 'score': 2},
  {'name': "Dexter", 'score': 2},
  {'name': "Mike", 'score': 2},
  {'name': "Pete", 'score': 2},
  {'name': "Dexter", 'score': 2}
]
score = 0
def countScores(ppl):
    result = {}

    for person in peeps:
        name = person.get('name')
        score = person.get('score')
        score += score
        result.update({name: score})
    return result

print(countScores(peeps))