#!/usr/bin/python
import csv

def write_primes(l,file_name):
    '''
    Writes number onto a csv file.

    Parameters:
        l(list): list of number wanting to write.
        file_name: name of the file wanting to write to.

    Result:
        Writes numbers from list onto file_name as a csv file
    '''
    with open(file_name, mode = 'w') as csvfile:
        primewriter = csv.writer(csvfile, delimiter = ' ')
        primewriter.writerow(l)
 
def read_primes(file_name):
    '''
    Reads numbers from a csv file.

    Parameters:
        file_name: name of the file wanting to read.

    Result:
        Reads numbers from a csv file and print them while putting a comma between each
    '''
    with open(file_name) as csvfile:
        primereader = csv.reader(csvfile, delimiter = ' ')
        for row in primereader:
            print(', '.join(row))
