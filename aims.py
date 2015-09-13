#!/usr/bin/env python
import math as mt
import numpy as np

def anything():
	return "Welcome to the AIMS module"


def main():
	print "Welcome to the AIMS module"

def mean(lst):
	'''calculates mean'''
	Sum = 0
	for i in range(len(lst)):
		Sum =Sum + lst[i]
	return Sum /len(lst)

def std(lst):
	'''calculates the standard deviation'''
	Sum = 0
	mn = mean(lst)
	for i in range(len(lst)):
		Sum  = Sum +mt.pow((lst[i]-mn),2)
	return np.sqrt(Sum/(len(lst)-1))


def avg_range('data/bert/audioresult-00215'):

    total = 0.0
    length = 0.0
    average = 0.0

    try:
        #Get the name of a file
        filename = data/bert/audioresult-00215

        #Open the file
        infile = open(filename, 'r')  

        #Read values from file and compute average
        for line in infile:
            print line.rstrip("\n")
            amount = float(line.rstrip("\n"))
            total += amount
            length = length + 1


        average = total / length

        #Close the file
        infile.close()

        #Print the amount of numbers in file and average
        print 'There were', length, 'numbers in the file.' 
        print format(average, ',.2f')

    except IOError:
        print 'An error occurred trying to read the file.' 

    except ValueError:
        print 'Non-numeric data found in the file'

    except:
        print('An error has occurred')

avg_range()



if __name__ == "__main__":
	main()
