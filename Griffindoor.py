jan = 31
feb = 28
mar = 31
apr = 30
may = 31
jun = 30
jul = 31
aug = 31
sep = 30
oct = 31
nov = 30
dec = 31

month = 0

print("Welcome to Griffindoor")
print("Month numbers: \nJan-1\nFeb-2\nMar-3\nApr-4\nMay-5\nJun-6\nJul-7\nAug-8\nSep-9\nOct-10\nNov-11\nDec-12")

choice = int(input("Enter month number: "))
times = choice

initial_gap = 2

gap = 2
choice = 0
if choice == 1:
    month = jan
    gap = 2
else:

    for i in range(1, times):

        choice = i

        if (choice == 1):
            month = jan
        elif (choice == 2):
            month = feb
        elif (choice == 3):
            month = mar
        elif (choice == 4):
            month = apr
        elif (choice == 5):
            month = may
        elif (choice == 6):
            month = jun
        elif (choice == 7):
            month = jul
        elif (choice == 8):
            month = aug
        elif (choice == 9):
            month = sep
        elif (choice == 10):
            month = oct
        elif (choice == 11):
            month = nov
        elif (choice == 12):
            month = dec

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
choice = times
if (choice == 1):
    month = jan
elif (choice == 2):
    month = feb
elif (choice == 3):
    month = mar
elif (choice == 4):
    month = apr
elif (choice == 5):
    month = may
elif (choice == 6):
    month = jun
elif (choice == 7):
    month = jul
elif (choice == 8):
    month = aug
elif (choice == 9):
    month = sep
elif (choice == 10):
    month = oct
elif (choice == 11):
    month = nov
elif (choice == 12):
    month = dec
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
