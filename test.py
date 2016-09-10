test = int(raw_input())
t = 0
while t<test:
	t =t+1
	name = raw_input()

	
	list = []
	list1 = []
	for x in name:
		list.append(x)
		
	lent = len(list)
	lent = int(lent/2)
	i = 0
	while i <(lent):
		if(i%2==0):
			m = list[i]
			list1.append(m)
		i =i+1
	print ''.join(map(str, list1))