months_arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print("Welcome to Griffindoor")
print("Month numbers: \nJan-1\nFeb-2\nMar-3\nApr-4\nMay-5\nJun-6\nJul-7\nAug-8\nSep-9\nOct-10\nNov-11\nDec-12")

choice = int(input("Enter month number: "))
temp = choice


gap = 2
choice = 0
if choice == 1:
    month = months_arr[0]
    gap = 2
else:

    for i in range(1, temp):

        choice = i
        choice -= 1
        month = months_arr[choice]

        mod_month = month
        mod_month += gap

        gap = 35-mod_month

        if (mod_month < 35):
            gap = 7-gap
        else:
            extra = mod_month - 35
            gap = extra

        if (gap < 0):
            gap *= -1

choice = temp
choice -= 1
month = months_arr[choice]
print("mon\ttue\twed\tthu\tfri\tsat\tsun")


for i in range(0, gap):
    print("\t", end="")

not_gap = 8-gap
for i in range(1, not_gap):
    print(i, end="\t")


pre_week = not_gap
nex_week = 7+not_gap
print("")
for i in range(0, 4):
    for j in range(pre_week, nex_week):
        if (j <= month):
            print(j, end="\t")
    print("")
    pre_week += 7
    nex_week += 7
