from pe_3 import tocompositeform

res=dict()

for i in range(2,21):
	ret=tocompositeform(i)
	d_ret=dict()
	for j in ret:
		if j not in d_ret.keys():
			d_ret[j]=ret.count(j)
	

	#merge res with d_rec
	keys=set(res.keys()) | set(d_ret.keys())
	vals=[max(res.get(n,0),d_ret.get(n,0)) for n in keys]
	res=dict(zip(keys,vals))
	print(res)

prod=1
for key,val in res.items():
	for j in range(val):
		prod*=key
print(prod)

