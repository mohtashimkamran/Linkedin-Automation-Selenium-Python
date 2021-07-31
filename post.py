i='daf'
x=list(i)
y=x
y.sort(reverse=True)
print(x,y,sorted(x))
if sorted(x)==x or x==y:
	print("y")
# 	m+=1
# else:
# 	c+=1