#pe_3

from math import sqrt
#eratosthenes sieve primality testing.
#if prime return 1 else 0

from pe_7 import notPrime

def sieve(test):
	sqroot=sqrt(test)
	i=3
	while i<=sqroot:
		if test%i==0:
			break
		i+=1
	else:
		return 1
	return 0

#prime number generator(or better validator )
#yields primes
def png(testfunc=sieve):
	yield 2
	
	test=3
	while(True):
		#if the testfunc is true yield
		try:
			if testfunc(test):
				yield test
		except notPrime:
			pass
		test+=2

def tocompositeform(N):
	
	if N==1:return [1]
	res=[]
	x=png()
	dv=x.__next__() #start the iterator
	while(N!=1):
		#not very efficient...sorry ^-^
		while(N%dv==0):
			res.append(dv)
			N/=dv
		dv=x.__next__()
	return res

