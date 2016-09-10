test_case = int(raw_input())
t = 0
b = 1
lista = []
list1 = []
list2 = []
list3 = []
list4 = []
while t<test_case:
	t=t+1
	inpu = raw_input()
	# i spilit the inpu in list and saved it to m and n
	inpu_list = inpu.split()
	m = int(inpu_list[0])
	n = int(inpu_list[1])
	a = m
	while a<(n+1):
		lista.append(a)
		a=a+1
	while b<n:
		b=b+1
		list1.append(2*b)
		list2.append(3*b)
		list3.append(5*b)
		list4.append(7*b)
	list1a = [x for x in lista if x not in list1]
	list1a = [x for x in list1a if x not in list2]
	list1a = [x for x in list1a if x not in list3]
	list1a = [x for x in list1a if x not in list4]
	print list1a		 