num = input("")
length = len(num)
num = int(num)
#print(length)

if length == 2:
    for i in range(num):
        t1 = i // 10
        t2 = i % 10
        if (t1 + t2)**2 == i:
            print(i)
if int(length) == 3:
    for i in range(2,num):
        if i > 9 and i < 100:
            t1 = i // 10
            t2 = i % 10
            if (t1 + t2)**2 == i:
                print(i)
        elif i >= 100:
            placeholder = i // 10
            t1 = placeholder // 10
            t2 = placeholder % 10
            t3 = i % 10
            if (t1 + t2 + t3) ** 3 == i:
                print(i)