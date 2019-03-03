range(1, 10, 2)
data = []
for r in range(1, 10,2):
	print (r)
	data.append(r)
print (data)
with open ('data.txt' , "w") as f:
	for d in data:
		f.write(str(d) + '\n')
