# Original array: [1, 2, 3, 4, 5, 6, 7, 8]
# Rotated array:  [2, 3, 4, 5, 6, 7, 8, 1]

num=int(input("Enter the number of elements : "))
arr=[]
for i in range(0,num):
    n=int(input("Enter the elements : "))
    arr.append(n)
print(arr)
arr1=[]
rot=int(input("Enter the rotation : "))
for i in range(0,rot+1):
    arr1.append(arr[i])
print(arr)
print(arr1)    
for i in arr1:
    arr.remove(i)
# arr2=[arr]-[arr1]
res=[arr2]+[arr1]
print(res)



