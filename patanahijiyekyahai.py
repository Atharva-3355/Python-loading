# # # # # str = "hello"www
# # # # # tup = ("Hello", 5 ,"a")
# # # # # list = [1 , 2 ,3]
# # # # # list[0] = 11
# # # sum = 0
# # # i = 0
# # # roww = int(input("Enter size:"))
# # # j = 0


# # # r1 = roww
# # # k = r1-1
# # # star = k
# # # for j in range(0, roww):

# # #     i = 1

# # #     for i in range(1, r1):
# # #         print(" ", end="")

# # #     r1 = r1-1

# # #     while (star < roww):
# # #         print("*", end="")
# # #         star += 1
# # #     print("")
# # #     k -= 2
# # #     star = k

# # # roww -= 1
# # # r1 = roww
# # # k = r1-1
# # # star = k

# # # for j in range(0, roww):

# # #     i = 1

# # #     while (star < roww):
# # #         print(" ", end="")
# # #         star += 1

# # #     for i in range(1, r1*2):
# # #         print("*", end="")

# # #     print("")

# # #     r1 = r1-1

# # #     k -= 1
# # #     star = k
# # for i in range(1, times):

# #     choice += 1

# #     pre_week = 1
# #     nex_week = 8

# #     if (choice == 1):
# #         month = jan
# #     elif (choice == 2):
# #         month = feb
# #     elif (choice == 3):
# #         month = mar
# #     elif (choice == 4):
# #         month = apr
# #     elif (choice == 5):
# #         month = may
# #     elif (choice == 6):
# #         month = jun
# #     elif (choice == 7):
# #         month = jul
# #     elif (choice == 8):
# #         month = aug
# #     elif (choice == 9):
# #         month = sep
# #     elif (choice == 10):
# #         month = oct
# #     elif (choice == 11):
# #         month = nov
# #     elif (choice == 12):
# #         month = dec

# #     for i in range(0, 5):

# #         for j in range(pre_week, nex_week):

# #             if (j <= month):

# #                 gap = 0

# #             else:
# #                 gap += 1

# #         print("")
# #         pre_week += 7
# #         nex_week += 7

# #     gap = 7
# #     initial_gap = gap

# # setting the no of days for all months in their respective variables

# # for j in range(1, 36):

# #         if (j <= month):

# #             gap = 0
# #         else:
# #             gap += 1
# jan = 31
# feb = 28
# mar = 31
# apr = 30
# may = 31
# jun = 30
# jul = 31
# aug = 31
# sep = 30
# oct = 31
# nov = 30
# dec = 31

# month = 0

# print("Welcome to Griffindoor")
# print("Month numbers: \nJan-1\nFeb-2\nMar-3\nApr-4\nMay-5\nJun-6\nJul-7\nAug-8\nSep-9\nOct-10\nNov-11\nDec-12")

# choice = int(input("Enter month number: "))
# times = choice

# initial_gap = 2

# gap = 2
# choice = 0

# for i in range(1, times):

#     choice = i

#     if (choice == 1):
#         month = jan
#     elif (choice == 2):
#         month = feb
#     elif (choice == 3):
#         month = mar
#     elif (choice == 4):
#         month = apr
#     elif (choice == 5):
#         month = may
#     elif (choice == 6):
#         month = jun
#     elif (choice == 7):
#         month = jul
#     elif (choice == 8):
#         month = aug
#     elif (choice == 9):
#         month = sep
#     elif (choice == 10):
#         month = oct
#     elif (choice == 11):
#         month = nov
#     elif (choice == 12):
#         month = dec

#     month += gap

#     gap = 35-month

#     if (month < 35):
#         gap = 7-gap
#     else:
#         extra = month - 35
#         gap = extra

#     if (gap < 0):
#         gap *= -1

#     print(gap)


#         print(month)
# print(choice)
# print("mon\ttue\twed\tthu\tfri\tsat\tsun")


# for i in range(0, gap):
#     print("\t", end="")

# not_gap = 8-gap
# for i in range(1, not_gap):
#     print(i, end="\t")


# pre_week = not_gap
# nex_week = 7+not_gap
# print("")
# for i in range(0, 4):
#     for j in range(pre_week, nex_week):
#         if (j <= month):


months_arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

choice = int(input("Enter Month no:"))
choice -= 1

month = months_arr[choice]
