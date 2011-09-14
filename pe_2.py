#pe_2
print("pe_2 imported\n")

def fastfib(value):
	n=0
	fib1=1
	fib2=1
	fib3=1
	while(fib3<=value):
		yield fib3
		fib3=fib1+fib2
		fib1=fib2
		fib2=fib3

def sumfun(N=4000000):
	sum=0
	for fib in fastfib(N):
		if (fib & 1)==0:
			sum+=fib
	return sum	
