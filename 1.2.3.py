records=[('foo',1,2),('bar','hello'),('foo',3,4),]
count=0
for tag, *args in records:
	count+=1
	print tag,args,count
