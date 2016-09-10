x = int(raw_input("Enter the value of x: "))
n = int(raw_input("Enter the value of n: "))
a = x
m = 1
# here m = 1 as we need to do this event n-1 times
while m<n:
	x=x*a
	m=m+1
print "Value of y is",x
