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

#Code with the help of Robin and myself
def avg_range(lst):
	#empty lists
	files = []
	ranges = []
	
	for location in lst:
		files.append(open(location))

	for entry in files:
		for line in entry:
			if "Range" in line:
				ranges.append(float(line[7]))
	return sum(ranges)/len(ranges)

if __name__ == "__main__":
	main()
