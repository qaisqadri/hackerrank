import re
nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
#print(matrix)
st=''
for y in range(m):
    for x in range(n):
        st=st+matrix[x][y]

st=re.sub("(?<=\w)([\W]+)(?=\w)"," ",st)
print(st)
