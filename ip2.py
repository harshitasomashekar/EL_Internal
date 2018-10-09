import sys
a=sys.argv[1]
with open('ip2.txt') as f:
	lines = f.readlines()
for x in lines:
	x=x.split(' ')
	if a == x[0]:
		print("IP found")
		break
	else:
		print("IP not found")
