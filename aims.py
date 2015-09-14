#!/usr/bin/env python
from __future__ import division
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

def avg_range(x):
	total = 0.0
	length = 0.0
	average = 0.0
	
	#taking file name
	filename = x
	
	#opening file
	infile = open(filename, 'r')
	
	#reading file
	contents = infile.read()
	for line in infile:
		amount = float(line)
		total += amount
		length = length + 1
	average = total / (length +1)
	infile.close()
	return average 


if __name__ == "__main__":
	main()
