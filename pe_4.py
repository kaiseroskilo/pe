#pe_4

def palindrome_test(N):
	s=str(N)
	l=len(s)
	start=0
	end=l-1
	while(start<=end):
		if s[start]!=s[end]:
			break
		start+=1
		end-=1
	else:
		return 0 #is palindrome
	return 1 #not palindrome

res=[]
max=0

for i in range(100,1000):
	for l in range(i,1000):
		sum=i*l
		if not palindrome_test(sum):
			res.append(sum)
			if max<sum:max=sum

print(max)
		
