from pickle import FALSE, TRUE


def is_prime(num):
    result = ""
    if num % 2 == 0:
        print("FALSE")
    else:
        for n in range(2,num):
            if num % n == 0:
                result = "FALSE"
                break
            elif not num % n == 0:
                result = "TRUE"

    print(result)

# num = int(input("enter num: "))

# is_prime(num)





def firstNPrimes(num):
    result = []
    for i in range (num):
        if i % 2 == 0:
            print()
        else:
            for n in range(2,i):
                if i % n == 0:
                    print("")
                elif not i % n == 0:
                    if (i == 25):
                        print()
                    elif (i not in result):
                        result.append(i)

    return result

# num = int(input("enter num: "))

# print(firstNPrimes(num))


def sumOfNPrimes(num):
    result = []
    for i in range (num):
        if i % 2 == 0:
            print()
        else:
            for n in range(2,i):
                if i % n == 0:
                    print("")
                elif not i % n == 0:
                    if (i == 25):
                        print()
                    elif (i not in result):
                        result.append(i)
    return sum(result)
 
num = int(input("enter num: "))

print(sumOfNPrimes(num))
