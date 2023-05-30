
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def countPrimes(n: int) -> int:
    count = 0
    if n <= 2:
        return count
    for i in range(2, n):
        if isPrime(i):
            count += 1
            i += 1
        else:
            i += 1
    return count


def countPrimes2(n: int) -> int:    # Sieve of Eratosthenes(Submitted)
    if n <= 1:
        return 0
    isPrime = [1] * n
    isPrime[0] = isPrime[1] = 0
    count = 0
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n, i):
                isPrime[j] = 0

    count = sum(isPrime)
    
    return count