def odd_range(num):
    result = []
    for n in range(num):
        if n%2 != 0:
            result.append(n)        

    return result

print(odd_range(8))