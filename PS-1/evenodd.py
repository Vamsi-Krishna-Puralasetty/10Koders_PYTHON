num = int(input("enter : "))

if num < 0:
    print("negative")
else:
    if num % 2 == 0:
        print("even")
    else: 
        print("odd")

# using ternary operator
print("even" if num % 2 == 0 else "odd")