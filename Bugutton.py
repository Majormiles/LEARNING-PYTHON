def primeFactor(num):

    arr = []
    for i in range (2, num):
        if (num % i) == 0:
            isPrime = True

            for j in range (2, i):
                if (i % j) ==0:
                    isPrime == False

                if isPrime == True:
                    arr.append(i)
    return len(arr)
print(primeFactor(575))
