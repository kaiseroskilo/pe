#pe_9.py
#DESCRIPTION
#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def fun(a,b):
	return a**2+b**2-(1000-a-b)**2

def nat_num(start=0):
	while(True):
		yield start
		start+=1

gen=nat_num(start=1)
b=gen.__next__()

bool=True
while(bool):
	for a in range(1,b+1):
		print("a={0} and b={1}".format(a,b))
		if fun(a,b)==0:
			print("a*b*c is {0}".format(a*b*(1000-a-b)))
			bool=False
			break
	b=gen.__next__()
	
