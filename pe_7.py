#pe_7
#
#DESCRIPTION
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import random


class notPrime(Exception):
	pass

def miller_rabin_test(n,k=10):

	#trivial cases
	primes={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71}
	if n in primes:
		return n
	if n%2==0:
		raise notPrime()
	n_1=n-1
	d=n_1
	s=0

	#write n-1=2^s * d ,where d is odd
	while(d%2==0):
		d=d/2
		s+=1
	
	#randomize,sys time
	random.seed()

	for i in range(k):
		a=random.randint(2,n-2)
		print(a)
		x=a**d % n
		if x==1 or x==n-1:
			continue
		for r in range(1,s):
			x=x**2 % n
			if x==1:
				raise notPrime()
			if x==n-1:
				continue
		raise notPrime()
	return n

