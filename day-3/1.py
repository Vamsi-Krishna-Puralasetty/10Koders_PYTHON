#Boolean=True or False.(Default=False)
#applications--> Atm pin, username and password
#  
#DATA TYPES
#numeric--!
#Sequences-->Strings,List,Tuple,Range.

#Array-->collections of homogeneous elements
#List in [] -->collection of heterogeneous elements
#list is mutable*****,can accept diff data types,indexing is possible
#ITERATION is slower in list**********
#List is not memory Efficient*****  

#Tuple-->collection of heterogeneous elements
#Tuple is IMMUTABLE****,can accept diff dat atypes,indexing is possible.
#ITERATION is faster in list**********
#Tuple is memory Efficient******

#Range--> (lower bound,upper bound)
#print(range(0,100))--> output is range(0,100)
#even num-->range(0,100,2)
#odd num-->range(1,100,2)



lst=[2,3,4,"str",False,[1,"bye",3]]
print(lst)
print(lst[3])
print(len(lst))
print(lst[5])
print(lst[-2])
print(lst[1:3:2])
# print(lst[6])
print(lst[-1][1])
lst[5][-1]="hello"
print(lst)
print(len(lst[5]))
print(len(lst))
print(len(lst[5][1]))
for i in range(0,len(lst)):
    print(lst[i])