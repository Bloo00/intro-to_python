
def is_prime(num):
    result = ""
    if num % 2 == 0:
        print("not prime")
    else:
        for n in range(2,num):
            if num % n == 0:
                result = "not prime"
                break
            elif not num % n == 0:
                result = "prime"

    print(result)

num = int(input("enter num: "))

is_prime(num)