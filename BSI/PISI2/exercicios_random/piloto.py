a, b, c = [int(i) for i in input().split()]

if (b-a) < (c-b):
    print("1")
elif (b-a) > (c-b):
    print("0")
else:
    print("-1")
