num = int(input("enter :"))

if num <= 0 or num > 7:
    print("cant display week")
else:
    if num==1:
        print("Monday")
    elif num==2:
        print("tuesday")
    elif num==3:
        print("wednesday")
    elif num==4:
        print("thursday")
    elif num==5:
        print("friday")
    elif num==6:
        print("saturday")
    else:
        print("Sunday")