#liður eitt
x = input("")
counter = 0

while x != "q" and x != "Q":
    
    for i in range(1,int(x)+1):
        if int(x) % i == 0:
            counter += 1
        
    if counter >= 10:
        print("yes")
        counter = 0
    else:
        print("no")
        counter = 0
        
    x = input("")

#liður tvö
num = input("")
length = len(num)
num = int(num)


if length == 2:
    for i in range(10,num+1): #skiptir tölum í tvennt og reiknar
        t1 = i // 10
        t2 = i % 10
        if (t1 + t2)**2 == i:
            print(i)
if int(length) == 3:
    for i in range(10,num+1): # !!!ATH!!! range er 10 af því að verkefnið biður um tveggja stafa heiltölu
        if i > 9 and i < 100: #sér um að skipta tveggja stafa tölum í tvennt og reiknar 
            t1 = i // 10
            t2 = i % 10
            if (t1 + t2)**2 == i:
                print(i)
        elif i >= 100: #skiptir þriggja stafa tölum í þrennt og reiknar út
            placeholder = i // 10
            t1 = placeholder // 10
            t2 = placeholder % 10
            t3 = i % 10
            if (t1 + t2 + t3) ** 3 == i:
                print(i)