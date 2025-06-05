# str = "hello"www
# tup = ("Hello", 5 ,"a")
# list = [1 , 2 ,3]
# list[0] = 11
sum = 0
i = 0
roww = int(input("Enter size:"))
j = 0

r1 = roww
k = r1-1
star = k
for j in range(0, roww):

    i = 1

    for i in range(1, r1):
        print(" ", end="")

    r1 = r1-1

    while (star < roww):
        print("*", end="")
        star += 1
    print("")
    k -= 2
    star = k

roww -= 1
r1 = roww
k = r1-1
star = k

for j in range(0, roww):

    i =1

    while (star < roww):
        print(" ", end="")
        star += 1

    for i in range(1, r1*2):
        print("*", end="")

    print("")

    r1 = r1-1

    k -= 1
    star = k
