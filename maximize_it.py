from itertools import product
def f(x):
	return x*x

def max_it(k,m,data):
	result=map(lambda x : [f(i) for i in x] ,product(*data) )
	res=[sum(x)%m for x in result]
	
	print(max(list(res)))





if __name__=='__main__':
	k,m=input().split()
	k,m=int(k),int(m)
	data=list()
	for a in range(k):
		i=input().split()
		c=int(i[0])
		if(len(i)-1) != c :
			exit()
		else:
			sd=list()
			for b in range(1,len(i)):
				sd.append(int(i[b]))
			data.append(sd)
	# print(k,m,data)
	max_it(k,m,data)


