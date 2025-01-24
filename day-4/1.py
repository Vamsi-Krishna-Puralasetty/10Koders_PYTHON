#Data Type::SEQUENCE
# Range--> 
# range(0,100)-->0 to 99
#range(100)-->0 to 99
#range(100,0,-1)-->100 to 1
#range(100,-1)-->empty list

#DATA Type:
#DICTIONARY {key:"value"}
#mutable
#same value can be given to different keys 
#same keys cannot be have different values
#duplicate keys are not allowed and if we give duplicate key, old value is updated by latest value will assigned to key
#new keys and values can be given and they will added at end of dict but if the key is already present the it wont be aiigned at the end but the key value will be updated by new assigned value to the key.
#


#DATA TYPE::
# SET {} --> individual elements separated by comma
#no keys and value pairs
#mathematically-->unordered,Finite,unique 
#python-->immutable,indexing is not possible
#order changes only after running the code or execution. multiple types printing before execution gives same order. 

dict={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f","g":7}
print(dict[1])
print(dict["g"])
dict[2]="bbb"
print(dict)
dict={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f","g":7,2:"abcd",5:"qwer","2":"abcd"}
print(dict)


#Data Type::
#NONE
#It occupies Space in memory
#It doesn't have any value to it.
#
num1=5
num1=None
print(num1)
print(type(num1))
print(id(num1))

#INPUT
#default input type is string
#Taking input from user or keyboard
# input("enter")-->Takes input and doesnt print it
# print(input("Enter a value :"))-->Takes input and prints it
num=input("Enter a value:")
print(num)
#int(input()) --> to convert input type to integer
#base 10 means decimal system


#!!number system

-----------------------------------------------------------------------------------------------

#Datatypes : strings,list,tuple,range,boolean

#List: it is a collection of elememts of different datatypes
my_list = [1,2,3,"str",["hey",-2,-4,0]]
print(type(my_list)) #<class 'list'>
print(my_list[0]) #1
print(my_list[-1]) #[-2,-4,0]
print(my_list[4][2]) #0
print(len(my_list)) #5
print(len(my_list[4][0])) #3

#Tuple: it is a collection of elememts of different datatypes but the main difference between list and tuple is it is immutable.
# list vs tuple:
# --> list is mutable whereas tuple is immutable
# --> list is slower whereas tuple is faster
# --> tuple's memory is more efficient as it is immutable so nothing changes
my_tuple1 = ()
my_tuple2 = (1,2,"heylo",24.5,(67,89,43),[78,"misty"])
print(my_tuple2[0]) #1
print(my_tuple2[4][2]) #43
print(my_tuple2[5][1]) #misty

# range : (lower,upper) --> lower(inclusive) && upper(exclusive)
# range(0,10)
# range(0,10,-1)
# range(0,10,2)
# range(10,0,-1)

#boolean : True or False 
# true --> 1
# false --> 0

# print(123=="123")