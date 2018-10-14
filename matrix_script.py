import re
import string
if __name__ == '__main__':
	nm = input().split()

	n = int(nm[0])

	m = int(nm[1])

	matrix = []

	for _ in range(n):
	    matrix_item = input()
	    matrix.append(matrix_item)
	# print(matrix)
	st=''
	for y in range(m):
		for x in range(n):
			st=st+matrix[x][y]

# print(st)
st=re.sub(r'(?<=\w)([\W]+)(?=\w)',' ',st)
# st=re.sub(r'[!@#$%&]'," ",st)
# st = re.sub(r'\s+', ' ', st)           # Eliminate duplicate whitespaces

print(st)