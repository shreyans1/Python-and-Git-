test_case = int(raw_input())
t = 0
list = []
while t<test_case:
	t=t+1
	inpu = raw_input()
	# i spilit the inpu in list and saved it to m and n
	inpu_list = inpu.split()
	m = int(inpu_list[0])
	n = int(inpu_list[1])
	if m==1:
		p=m+1
	else:
		p=m	
	w = n+1
	while p<(n+1):
		i = 2
		flag = 0
		while i<p:
			if p%i==0:
				flag = 1
				break
			i =i+1	
		if flag==0:
			list.append(p)

		p=p+1
	l = len(list)
	a = 0
	while a<l:
		print int(list[a])
		a = a+1

	list = []