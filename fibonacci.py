# Fibonacci Sequence, all numbers < 100
# -------------------------------------------

x = [1,1]
flag = False
i = 2
while flag is False:
	temp = x[i-1]+x[i-2]
	if temp < 100:
		x.append(temp)
	else:
		flag = True
	i=i+1

print(x)

# Fibonacci Sequence, first 20 numbers
# -------------------------------------------

x = [1,1]
flag = False
i = 2
for i in range(20):
	x.append(x[i-1]+x[i-2])

print(x)

