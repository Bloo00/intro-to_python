from pickle import FALSE, TRUE


def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        else:
            return True

num = int(input("enter num: "))

print(is_prime(num))





def firstNPrimes(num):
    arr = []
    test=1
    if num == 0:
        return arr

    while(len(arr)< num):
        if (is_prime(test)):
            arr.append(test)
        test+=1
    return arr

num = int(input("enter num: "))

print(firstNPrimes(num))


def sumOfNPrimes(num):
    return sum(firstNPrimes(num))
 
num = int(input("enter num: "))

print(sumOfNPrimes(num))
