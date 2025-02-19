# #scope - Global, local
# # Global scope -  life time is entire code
# # Local scope - life time is until the function runing or existance
# # scope -  where you can acces the variable

# num_1 = 15
# def check_scope():
#     # num_2 = 35
#     num_1 = 4
#     print(num_1)
#     # print(num_2)

# check_scope
# print(num_1)
# # print(num_2)



# # by Global keyword already declare variable outside function will be manipulated. and no need of creating any new variable in the function
# num_1 = 15
# def check_scope():
#     # num_2 = 35
#     global num_1
#     num_1 = 4
#     print(num_1)
#     # print(num_2)

# check_scope
# print(num_1)
# # print(num_2)


# # num_1 to be both local and global 
# num_1 = 15
# def check_scope():
#     # num_2 = 35
#     num_1 = 32
#     globals()['num_1'] = 45    #to change the global variable to local variable
#     num_1 = 4
#     print(num_1)     # 32
#     # print(num_2)

# check_scope
# print(num_1)   # 45
# # print(num_2)


# inbuilt functions : 


# replace() ->
# Creates a new string and old string is not manipulated
str = "being human"
print(str.replace('human','living'))
print(str)



# remove() ->
# we need to give the element/value not its index.
# removes the first occurance of an element
# if value is not in list -> Value Error
# First check for the availability of the element in the List.
lst = [1,2,3,4]
lst.remove(3)
print(lst)

lst1 = [1,2,2,2,3,4]
lst1.remove(2)
print(lst1)



# case changing ->
str1= "vamsi krishna 01"
str2= (str1.upper())
print(str2)   # VAMSI KRISHNA 01
print(str2.lower())   # vamsi krishna 01



