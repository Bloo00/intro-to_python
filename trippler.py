from unittest import result


def trippler(arr):
    result = []
    for num in arr:
        result.append(num*3)
    return result


print(trippler([123,123,123]))