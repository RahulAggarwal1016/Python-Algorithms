"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Implementing Sieve Sorting: https://www.geeksforgeeks.org/segmented-sieve/ 
"""

def sieve(num):
	if num < 1:
		return []
	else:
		primes = [False, False] + [True] * (num-1)

		if num < 2:
			return []
		else:
			for i in range(2, int(num**0.5)+1):
				if primes[i]:
					for j in range(i*i, num, i):
						primes[j] = False
			else:
				return [i for i in range(num+1) if primes[i]]