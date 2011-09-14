#pe_3

from math import sqrt

#prime number generator(or better validator )
#yields primes
def png():
	yield 2
	
	test=3
	while(True):
		sqroot=sqrt(test)
		i=3
		while i<=sqroot:
			if test%i==0:
				break
			i+=1
		else:
			yield test
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
		
