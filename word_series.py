####### Word Series Program #######
### Author: Pallavi

#Importing the modules
import collections
from string import ascii_lowercase as al
#Creating a Ordered Dictionary
d = collections.OrderedDict((y,x) for x,y in enumerate(al,1))
#Creating a list for the keys
li = d.keys()
for i in range (1,len(li)):
	tmp =  li[i]
	tmp1 = li[i-1]
	d[tmp] = int(d[tmp1]*2+i+1)
print "\n Key \tValue"
for k in d:
	print k,"\t",d[k]

str1 = raw_input("\nEnter a string : ")
#print str1
sum = 0
str11 = str1.lower()
for i in str11:
	print i,d[i]
	sum = sum+ int(d[i])
print "Sum of Characters in given string %s:%s"%(str1,sum)
list1 = d.values()
st = []
maxweight = int(input("Enter a Number : "))
m = maxweight
for i in range(len(d),0,-1):
	t = list1[i-1]
	while t <= maxweight:
		maxweight = maxweight-t
		st.append(t)

#print st
#print maxweight
str1 = ""
for i in st:
	for key in d:
		if i == d[key]:
			str1 = str1+key
print "Shortest Strings of letters corresponding to %d : %s"%(m,str1)

