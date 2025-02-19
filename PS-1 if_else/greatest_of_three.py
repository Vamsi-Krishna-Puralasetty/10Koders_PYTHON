def greatest_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

print(greatest_of_three(4,2,9))