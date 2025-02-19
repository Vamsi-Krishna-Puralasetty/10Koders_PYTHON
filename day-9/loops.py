# for loop and while loop

# ************FOR LOOP*******************
# # ---------print 0 to 20 ---------
# for y in range(0,21):
#     print(y)
#     print("Edho okati")
#     print("Malli edho okati")
# # ------print 5 to 25(method-1)---------
# for y in range(0,21):
#     print(y+5)
#     print("Edho okati")
#     print("Malli edho okati")
# # ------print 5 to 25(method-2)---------
# for y in range(5,26):
#     print(y)
#     print("Edho okati")
#     print("Malli edho okati")

# # ------- odd and even using loop and if ---------
# # method -1
# for i in range(0,21):
#     if i%2==0:
#         print(i, 'Even')
#     else:
#         print(i, 'odd')
# # method-2
# ---- even -------
# for i in range(0,21,2):
#     print(i)
# ---- odd ------
# for i in range(1,21,2):
#     print(i)

# # ---------multiples of 3 --------
# # method-1
# for i in range(0,21,3):
#     print(i)
# # method-2
# for i in range(0,21):
#     if i % 3 == 0:
#         print(i)

# --------squares of natural numbers -----------
# for i in range(0,100):
#     print(i*i*i)
#     print(i**2)

# **********NESTED FOR LOOP*************
# # print roll no. of students in 10 classes
# for j in range(1,11):
#     for i in range(1,31):
#         print(j,i)
# # -------to skip 5th --------------
# for j in range(1,11):
#     for i in range(1,31):
#         if j != 5:
#             print(j,i)
# # -------to skip 5th and 7th class ---------
# method-1
# for j in range(1,11):
#     for i in range(1,31):
#         if j != 5 and j != 7:
#             print(j,i)
# method -2(more efficient)
# for j in range(1,11):
#     if j != 5 and j != 7:
#         for i in range(1,31):
#             print(j,i)

# *************WHILE LOOP ***************************************
# loop continues till the condition fails.
# ITERATES ONLY THE CONDITION IS TRUE AND UNTIL CONDITION IS TRUE.
# ITARATION STOPS WHEN CONDITION TURNS FALSE.
# Example :- while i am going home, i was watching a movie.
# ----------syntax : -----------------
# while condition:
#     print("kill......")
#     print("still fighting")

# num1=10
# while num1<5:
#     print("kill......")
#     print("still fighting")

# num1=4
# while num1<5:
#     print("kill......")
#     print("still fighting")
# output is print infinite times.
# num1=2
# while num1<5:
#     print("kill......")
#     print("still fighting")
#     num1+=1
# prints 3 times of while loop



# FOR LOOP VS WHILE LOOP
# if range is known or number of iterations is known tyhe use for loop.
        #ex: i will pay bill to these number of people
# condition is known and number of iterations is unknown then use while loop.
        # ex: i will pay the bill until in have the money(here exact number is not known).

# *********for loop to while loop **********
# ----------even and odd---------
# start = 5
# while start < 26:
#     if start % 2 == 0:
#         print(start ,'even')
#     else:
#         print(start ,'odd')
#     start += 1

# # print roll no. of students in 10 classes
# # -------to skip 5th and 7th class ---------
start1=1
while start1 < 11:
    start2=1
    if start1 != 5 and start1 != 7:
        while start2 < 31:
            print(start1,start2)
            start2 += 1
    start1 +=1






