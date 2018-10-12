# https://www.hackerrank.com/challenges/ginorts/problem

def ginorts(s):
	#st=list(s)
	length=len(s)
	upper=list()
	lower=list()
	nume=list()
	numo=list()
	for x in s:
		if x.isupper():
			upper.append(x)
		elif x.islower():
			lower.append(x)
		elif x.isdigit() and int(x) % 2 == 0:
			nume.append(x)
		elif x.isdigit() and int(x) % 2 != 0:
			numo.append(x)
	upper.sort()
	lower.sort()
	nume.sort()
	numo.sort()
	
	s=''
	for x in lower:
		s=s+x
	for x in upper:
		s=s+x
	for x in numo:
		s=s+x
	for x in nume:
		s=s+x
	print(s)		
			
		


if __name__=="__main__":
	s=input()
	ginorts(s)
