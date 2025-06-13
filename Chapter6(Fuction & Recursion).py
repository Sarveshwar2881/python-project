# How to write function?
# aapke more line of code ko short krne ke liye fuction ka use hota hai.
# For normal sum
# def calc_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# calc_sum(5,25)              #PH==== 30, 8200 next line me
# calc_sum(575,7625)          

# More small for plus
# def calc_sum(a,b):
#     return a+b
# add=calc_sum(144,256)
# print(add)                      #PH=== 2300

# for difference
# def calc_diff(a,b):
#     return a-b
# diff=calc_diff(144,115)
# print(diff) 

# # for multiply
# def calc_multi(a,b): 
#     return a*b
# multi=calc_multi(14,6)
# print(multi)

# # for divide
# def calc_divide(a,b):
#     return a/b
# divide=calc_divide(144,2)
# print(divide)

# for modulo
# def calc_Modulo(a,b):
#     return a%b
# Modulo=calc_Modulo(144,20)
# print(Modulo)

# # for Average
# def calc_avg(a,b,c,d,e):    
#     sum=a+b+c+d+e
#     avg= sum/5
#     print(avg)
#     return avg

# asd=calc_avg(45,89,67,77,85)

# print("apnacollage")
# # for space in between 2 stings as like ("string","string")
# print("sarvesh","kumar")
# print multipul parmeters in 1 line.
# print("apnacollage", end=" ") 
# print("sarvesh")
# print("kumar")

# print ("This is a bug but developer is not understand tnis.")
# print ("This is a bug but developer is not understand tnis.")

# What is default parameters?

# write a fuction to print the length of list? (List is the parameter)
# nums=[1,2,3,4,5,6,7,8,9,10,5,4,4564,5,4,89,99,54,67]
# def print_len():
#     print(len(nums))
# print_len()
    
# Heros=["tiger","rakhi","mohit","batman","hitman"]
# def heros_name():
#     print(len(Heros))
# heros_name()

# nums=(1,2,3,4,5,6,7,8,9,10,5,4,4564,5,4,89,99,54,67,)
# Heros={"tiger":"rakhi","mohit":"batman","hitman":12345}
# print(*nums,*Heros,end=" ")

# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 4564, 5, 4, 89, 99, 54, 67)
# Heros = ["tiger","rakhi", "mohit", "batman", "hitman"]
# print(*nums, *Heros, end=" ")

# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 4564, 5, 4, 89, 99, 54, 67)
# Heros = ["tiger","rakhi", "mohit", "batman", "hitman"]

# def length_of_list(value):
#    print(len(value))    

# length_of_list(Heros)
# length_of_list(nums)                                                                      

# how to print any one value form list and tuple and string and dictionary and sets.
# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 4564, 5, 4, 89, 99, 54, 67)
# Heros = ["tiger","rakhi", "mohit", "batman", "hitman"]
# dict={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 4564, 5}
# value={1:2, 3:4, 5:6, 7:8, 9:10, 5:4, 45:5}

# dict_list = list(dict)
# value_list = list(value)
# print(nums[12],Heros[3],dict_list[9],value_list[4], end= " ")

#  if any sign is appearing in list of end in printed list then print in last with parnthahis.print()

# Factorial kya hota hai. "!" this is the sign of factoral. 5! ka factorial 5*4*3*2*1= 120

# def cal_fact(n):
#     fact=1
#     for i in range (1, n+1):
#         fact *=i
#     print(fact)
# cal_fact(7)

# Q==4 waf convert USD to INR.

#my way
# def convt_usd(USD):
#     UsdValue=USD * 85
#     print("USD=",UsdValue)

# convt_usd(2)

# shradha khapra way


# def converter(usd_inr):

#     inr_val = usd_inr * 85
#     print(usd_inr,"USD = INR",inr_val)

# #usd_input = float(input("Enter USD: "))

# converter(54)

# REUCRSION -- as like loop's big brother.
# if u want print 10,9,8,7,6,5,4,3,2,1(for revers counting)
# def show(n):
#     if n==0:
#         return
#     print(n)
#     show(n-1)
# show()

# Use of factorial in programming.
# def fact (n):
#     if (n==1):
#         return 1    
#     return fact (n-1)*n

# print(fact(20))

# factorial Question 1
# write a recursive function to calculate the sum of first n natural numbers.
# SUM of n number.
# def calu_sum(n):
#     if n==0:
#         return 0
#     return calc_sum(n-1) + n
































    
