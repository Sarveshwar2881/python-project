
# print("hi this my table ")

# i=1
# while i<=10:
#     j=1
#     while j<=10:
#         print(i*j ,end="\t")
#         j=j+1
#     print()
#     i=i+1
# Gap de de ke table.
# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print(i * j, end="\t")  
#         j = j + 1
#     print()  
#     i = i + 1

# index = 0

# print("Odd numbers:")
# while index < len(numbers):
#     if numbers[index] % 2 != 0:
#         print(numbers[index])
#     index += 1



# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# index = 0
# while index < len(my_list):
#   number = my_list[index]
#   if number % 2 == 0:
#     print(f"{number} is even")
#   else:
#     print(f"{number} is odd")
#   index += 1

#   def calculate_ticket_price(age, day_of_week):
#   """
#   Calculates the ticket price based on age and day of the week.

#   Args:
#     age: The age of the person.
#     day_of_week: The day of the week (e.g., "Monday", "Tuesday", "Wednesday").

#   Returns:
#     The ticket price in rupees.
#   """

#   if age < 18:
#     ticket_price = 8
#   else:
#     ticket_price = 12

#   if day_of_week == "Wednesday":
#     ticket_price -= 2

#   return ticket_price

# # Example usage:
# age = 17
# day = "Monday"
# price = calculate_ticket_price(age, day)
# print(f"Ticket price for a {age} year old on {day}: {price} rupees")

# age = 20
# day = "Wednesday"
# price = calculate_ticket_price(age, day)
# print(f"Ticket price for a {age} year old on {day}: {price} rupees")

# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1151, 10, 11, 12, 1823, 13, 14, 15, 1823, 1823]
# target = 1823
# i = 0
# Found = False
# while i < len(list):
#     if list[i] == target:    
#         print("Found")                
#         Found = True
#         break    
#     i += 1
 
# if not Found:
#     print("Not Found")
# list = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 1151,10, 11, 12,1823, 13, 14, 15,1823,1823]
# i = 0 
# num=1823
# while i < len(list):
#  if i ==num:
#         print("found",i)
#         break
        
# else:
#        print("not found")

# i+=1 
 
# for i in list:
   
#     if i==num:
#         print("found",i)
#         break
# else:
#      print("not found")

# bracket=[1,5,8,6,16,49,78,81,96,101,240,160,850.7001]
# i=0
# flag = False
# while i<len(bracket):
#     if(bracket[i]==8):
#         flag = True
#         break
#     i=i+1
# if(flag):
#     print("Found at index : ", i)
# else:
#     print("Not found")


# find x value in tuple.
# nums=(1,5,8,6,16,49,78,81,96,101,49,240,160,49,850.7001)
# x=49
# i=0
# while i < len(nums):
#     if nums[i] == x:
#         print(nums[i],"Found its Index:-:",i) 
#     else:
#         print("find continuing")
#     i=i+1 


# how to use break with simple loop?
# i=0
# while i<= 5:
#     print(i)
#     if (i==3):
#         break
#     i=i+1
# print ("The End Of Loop")


# how to user break 2nd postion.
# nums=(1,5,8,6,16,49,78,81,96,101,49,240,160,49,850.7001,1,5,8,6,16,49,78,81,96,101,49,240,160,49,850.7001)
# x=49
# y=0
# i=0
# while i < len(nums):
#     if nums[i] == x:
#         print(nums[i],"Found its Index:-:",i) 
#         y=y+1
#     if  y==6:
#         print("10nd found")
#         break
#     else:
#         print("Not Found")
#     i=i+1 

# how  to Use continue with simple loop?
# i=0
# while i<=5:
#     if i ==3:                   # 3 is the skip form the output.
#         i=i+1                   # continue with +1, 3+1=4 se continue.
#         continue                # Continue is continue.
#     print(i)
#     i=i+1

# how to print odd number in number of 1to 10.
# i=0
# while i<=10:
# #     if i%2==0:
# #         i=i+1
# #         continue
# #     print(i)
# #     i=i+1
#     if i%2 !=0:
#         i=i+1
#         continue
#     print(i)
#     i=i+1

# how to use for loop in simple code.
# list=[1,2,3,4,5]
# for el in list:
#     print(el)

# fruites instead of numbers.
# list=["Mango","Apple","Banana","Grapes","Watermilon"]
# for item in list:
#     print(item)
#
# How to print in tuple
# tup=(1,4,7,11,10,19,25)
# for el in tup:
#     print(el)
    
# How to print string characters.?
# str="SARVESHWAR"
# for chr in str:
#     print(chr)

# Use of else?
# str="Sarveshwar"
# for el in str:
#     print(el)
# else:
#     print("End the code.")

# Use else in break condition.
# str="Sarveshwar"  # finding (v)
# for el in str:
#     if el == "v":
#         print("v-found")
#         break
#     print(el)
# else:
#     print("Finding End")

# Question 1
# Print the elements of the following list useing a loop?

# list=[1,4,9,16,25,36,49,64,81,100]
# for el in list:
#     print(el)

# Question 2  (linear search--i single line ke ander search kerta hai.)
# Search for a number x in this tuple using loop?
# tup=(1,4,9,16,25,36,49,64,81,100,36)
# x=36
# idx=0
# for el in tup: 
#     if el == x:
#         print(x,"found of index:-",idx)
#         idx=idx+1

# str="Sarveshver"  # finding (v)
# chr="v"
# index = 0


# for i in range(len(str)):
#     if(chr==str[i]):
#         print("index=",i)
#         index=index+1
#     if(index==2):
#         print("Stop")
#         break   
#     if(index==0 and (len(str)-1)==i):
#         print("Item not found.")

# str="Sarveshver"  # finding (v)
# chr="v"
# index = 0
# for el in str:
#     if el == "v":
#         print("v-found")
#         break
#     print(el)
# else:
#     print("Finding End")

# str = "SarveshvarRishi"
# char = "Z"
# index = 0
# for i in range(len(str)):
#     if str[i].lower() == char.lower() :
#         print("Character", str[i], "found at index", i)
#         index += 1
#         if index == 2:
#             print("stop")
#             break
# else:
#     print("Character Not Found")

# # Range Function
# print(range(5))                 # PH range(0, 5)

# seq=range(1,6)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])
# print(seq[5])

# seq = range(10)
# for i in seq:
#     print(i)

# for seq in range(10):         # 10 is stopping condition -1
#     print(seq)              # PH 0,1,2,3,4,5,6,7,8,9

#for seq in range(2,10):         # 2 is stating and 10 stopping condition -1
#    print(seq) 

# for seq in range(2,10,2):         # 2 is stating and 10 stopping condition -1, and 2 is step 
#         print(seq)              # PH 2,4,6,8
    
# for seq in range(2,50,2):         # print even(2,4,6) number in between 2 to 50 count. 
#     print(seq) 

# for seq in range(1,50,2):         # print odd(1,3,5) number in between 2 to 50 count. 
#     print(seq)
        
# practice question
# First-- print number from 1 to 100.
# for i in range (1,101):
#     print(i)

# # Second-- print number from 100 to 1.
# for i in range (100,0,-1):
#     print(i)

# Third-- print the multiplication table of number n.
table = int(input("enter table write you want:-"))
for i in range(1,11):
    print(table*i)        