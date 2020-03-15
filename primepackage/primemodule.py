#!/usr/bin/python

def isPrime(n):
    '''
    Determines if a number is prime or not.

    Parameters:
        n(int): to determine if integer is prime.

    Result:
        Returns True if number is prime, False if number is not prime.
    '''
    if(n == 0 or n == 1):
        return False
    for i in range(2,n):
        if(n % i == 0):
            return False
        else:
            return True


def getNPrime(num):
    '''
    Creates a list of prime numbers

    Parameters:
        num(int): Number of prime number wanted.


    Result:
        Adds num to a list(primes) if it is prime. Returns primes.
    '''
    count = 0
    primeCount = 0
    primes = []
    while primeCount != num:
        if isPrime(count):
            primes.append(count)
            primeCount += 1
        count += 1
    return primes