# # Jump statements - break , continue , pass

# # Break and continue are used in loops

# # BREAK - if break statement is executed the loop stops immediately
# # -> ENTIRE loop stops even condition is true also
# -> Break applies to only one single for loop not any other parent loops--------------------------------------
# # if the break executed for first iteration of loop then the loop doesnt run for remaining elements
# for i in range(0,31):
#     break   #o/p -> loop runs for only one time and gets breaked but doesnt run for remaining 29 elements

# for i in range(0,21):
#     if i % 2 == 0:
#         print(i)   # o/p -> 0 2 4 6 8 10 12 14 16 18 20
#     if i == 9:
#         break   # o/p -> 0 2 4 6 8


# for i in range(0,21):
#     if i % 2 == 0:
#         print(i)   # o/p -> 0 2 4 6 8 10 12 14 16 18 20
#     # if i == 1:
#         # break    # o/p -> 0  first 0 is printed and then enters the second loop and gets breaked
#     if i == 0:
#         break    # o/p -> 0    first 0 is printed and then enters the second loop and gets breaked


# for i in range(0,21):
#     if i == 0:
#         break     #o/p -> no output - the 0 enters the first loop and gets breaked so it doesnt enter the second loop
#     if i % 2 == 0:
#         print(i)   
    
# # if the break executed for first iteration of loop then the loop doesnt run for remaining elements
# for i in range(0,31):
#     break   #o/p -> loop runs for only one time and gets breaked but doesnt run for remaining 29 elements

# for i in range(0,31):
#     if i == 2:
#         break   #o/p -> loop runs for 3 iterations

# for i in range(0,31):
#     if i == 2 or i == 5: 
#         break    #o/p -> loop runs for 3 iterations



# # CONTINUE - IF CONTINUE statement executes only that iteration is stopped and other iterations will be running in the loop

# for i in range(0,10):
#     if i == 5:
#         continue #for i==5 the next lines doesnt gets executed and remaining i values will be executed
#     print(i)


for i in range(0,10):
    print(i,"Iteration")
    if i == 5 or i == 6:
        continue
    print(i)

for i in range(0,20):
    continue   # loop executes for 20 times 
    # break # loop executes for 1 time

for i in range(0,20):
    continue 
    break   #this loop executes for 20 times