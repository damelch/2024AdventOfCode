from collections import Counter

text_file = open("day1.txt", "r")

#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()

col1 = []
col2 = []

nlist = data.split('\n')
nlist.pop()

for i in nlist:
    num = i.split()
    col1.append(num[0])
    col2.append(num[1])


col1 = [int(x) for x in col1]
col2 = [int(x) for x in col2]
col1.sort()
col2.sort()

diff = 0

for i in range(len(col1)):
    diff = diff + abs(col1[i] - col2[i])

sim = 0
ccol1 = Counter(col1)
ccol2 = Counter(col2)
print(ccol1)

for key in ccol1:
    if key in ccol2:
        sim = sim + (key * ccol2[key])

print(sim)

