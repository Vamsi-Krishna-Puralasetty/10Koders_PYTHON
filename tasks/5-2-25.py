# 1. print 1 to 100 numbers using while loop
# 2. print 1 to 100 in reverse order using for Loop and while loop
# 3. reverse a number using while loop without string conversion
# 	i/p : 1234
# 	o/p : 4321

# Question - print 1 to 100 numbers using while loop
num=1
while num<101:
    print(num)
    num+=1

#Question - print 1 to 100 in reverse order using for Loop and while loop
# for loop
# for i in range(100,0,-1):
#     print(i)

# while loop
num=100
while num>0:
    print(num)
    num-=1

#question - reverse a number using while loop without string conversion
# 	i/p : 1234
# 	o/p : 4321
# -------------------method - 1 ------------------
num=1234
temp=num
len=0
while temp>0:
    temp=temp//10
    len+=1
res=0
# count=len
while num>0:
    res+=(num%10)*(10**(len-1))
    num=num//10
    len-=1
print(res)
# -------------------method - 2 -------------------
num = 1234
rev = 0
while num>0:
    last = num%10
    rev = rev * 10 + last
    num//=10
print(rev)




