#nested conditions
a=0
if a>0:
    if a%2==0:
        print("a is postive and even integer")
    else:
        print("a is postive number")
elif a==0:
    print('a is zero')
else:
    print('a is a negative number')