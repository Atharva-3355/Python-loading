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


if (choice == 1):
    month = jan
    gap = 2
elif (choice == 2):
    month = feb
    gap = 5
elif (choice == 3):
    month = mar
    gap = 5
elif (choice == 4):
    month = apr
    gap = 1
elif (choice == 5):
    month = may
    gap = 3
elif (choice == 6):
    month = jun
    gap = 6
elif (choice == 7):
    month = jul
    gap = 1
elif (choice == 8):
    month = aug
    gap = 4
elif (choice == 9):
    month = sep
    gap = 0
elif (choice == 10):
    month = oct
    gap = 2
elif (choice == 11):
    month = nov
    gap = 5
elif (choice == 12):
    month = dec
    gap = 0


print("mon\ttue\twed\tthu\tfri\tsat\tsun")


not_gap = 8 - gap
pre_week = not_gap
nex_week = 7 + not_gap

for i in range(0, gap):
    {
        print("\t", end="")
    }

for i in range(1, not_gap):
    {
        print(i, end="\t")
    }

print("")

for i in range(0, 4):

    for j in range(pre_week, nex_week):

        if (j <= month):
            {
                print(j, end="\t")
            }

    print("")
    pre_week += 7
    nex_week += 7
