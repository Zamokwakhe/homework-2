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



if __name__ == "__main__":
	main()
