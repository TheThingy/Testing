value = int(input("Enter number: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lowlist = []

if value >= 1:
    for x in a:
        if x <= value:
            lowlist.append(x)
    print(lowlist)
else:
    print("number cannot be lower than 1")
