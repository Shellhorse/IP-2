#!/usr/bin/python

from primepackage import *

def main():

    primes = getNPrime(100)

    write_primes(primes, 'output.csv')

    l = read_primes('output.csv')

    print(l)

if __name__ == '__main__':
    main()    
