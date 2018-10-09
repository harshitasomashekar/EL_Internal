import sys
count=0
a=sys.argv[1]
with open('ip.txt') as f:
	lines = f.readlines()
for x in lines:
	x=x.split('\n')
	if a == x[0]:
		count=count+1
		print("IP is present",count,"times")
		break
	else:
		print("IP not found")


