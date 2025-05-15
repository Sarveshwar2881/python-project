# 2 types of lool 1st while loop and 2nd for loop. 
# In loop condition is checked again and again when it is completed.


# how to print any table.
# user_input = int(input("Enter your Number, which want to you write table : "))

# for number in range (1,2*6-1):
#     print(user_input * number)

# how to print infinite time hello
# while True :
#  print("Hello : Sarveshwar Kumar")
#  print("Address : Mansorver Park")
#  print("Working : Vivo Collobroation")
#  Regular print these


# How many times you want to print Hello word (as like 6) with out numbering
# count=1
# while count <= 6 :
#     print("Hello Word")
#     count = count + 1

# How many times you want to print Hello word (as like 6) with numbering
# count=1
# while count <= 6 :
#     print(count,"Hello Word")
#     count = count + 1

# how many times hello print check.
# count=10
# while count <= 10-5 :
#     print("Hello Word")
#     count = count + 1
# print(count)

# print number form 1 to your choise number (Counting) this time 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1

# for Reverse value 

# infinite loop do not create it.
# i = 5
# while i < 6:
#     print(i) 
#     i-=1

# How to print 1 to 100? and 
# i=1
# while i <=100:
#  print(i)
#  i +=1
#reverse 100 to 1?
# i=100
# while i >=1:
#  print(i)
#  i -=1
# For print both to-geather.
# i=1
# while i <=100:
#   print(i)
#   i +=1
# #reverse 100 to 1?
# i=100
# while i >=1:
#  print(i)
#  i -=1

# How to write any table.
# table = 1
# while table <=10:
#     print(table*5)
#     table +=1

# pratices for any table 
# t=1
# while t <= 10:
#   print(t*2)
#   t+=1
# Table print with numbring.
# t=1
# while t <= 10:
#  print(t,t*2)
#  t+=1
# print all table togeather.

 
# Table = int(input ("Enter table number you want to:-"))
# t = 0
# while t <=9:
#     #print(t,t*8)
#     t+=1
#     print(t, "x" ,Table, "=" ,Table*t)

# For 3,4 table
# a = 1
# while a<= 10:
#     print(a*3,a*4)
#     a= a+1

# Input with table.
# n=int(input("Enter Table number you want to print:-"))
# a = 1
# while a<= 10:
#     print(a*n)
#     a= a+1
 
# Question --4
# list=[1,4,9,16,25,36,49,64,81,100]
# print(list[0])
# print(list[1])
# print(list[3])
# print(list[4])
# print(list[5])
# print(list[6])
# print(list[7])
# This is way to print list type.(above)
# if you want to print from while loop.(under)

# list=[1,4,9,16,25,36,49,64,81,100]
# index=0
# while index < len(list): 
#     print(list[index])
#     index = index+1

# list=[1,4,9,16,25,36,49,64,81,100]
# Hero=["HHH","Under Taker","Shown Mical","Batista","Stone Gold"]
# # index=0
# # while index < len((list)): 
# #      print(list[index])
# #      index = index+1 
# index=0
# while index < len((list,Hero)):
#     print(Hero[index])
#     index= index+1
#     print(list[index])
#     index= index+1
#n=8
# t = 1
# while t <=10:
#     print(t*4)
#     t+=1
#     # print(t, "x" ,t, "=" ,t*n)
#     # t=t+1
# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# oddnum = []
# evennum = []
# i = 1
# while i<=len(list):
#     if i%2 == 0:
#         evennum.append(i)
#     else:
#         oddnum.append(i)
#     i += 1

# print ('Even Numbers are: ', evennum)
# print ('Odd Numbers are: ', oddnum)

list = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 1151,10, 11, 12,1823, 13, 14, 15,1823,1823]
i = 0  
while i < len(list):
    if list[i] == 1823:
        print(list[i])
        print("Value of index : ",i)
        break
    i = i + 1
    
# else:
#     print("not found")

    




# Codition:- if age is above to 18 then ticket price is 12 and age is blow to 18 then ticeket 
# price 8. if day wednesday then ticket price -2 ruppes.
# age=int(input("Enter Age:-"))
# day=input("Enter day:-")
# if age < 18:
#     price = 8 
# else:
#     price = 12
# if day == "wednesday":
#     price-=2
# print("Price:", price)

#list=(1,4,9,16,25,36,49,64,81,100)
# Hero=("HHH","Under Taker","Shown Mical","Batista","Stone Gold")
# idx= 0
# while idx < len(list): 
#     print(list[idx])
#     idx = idx+1 

# list=[1,4,9,16,25,36,49,64,81,100]
# Hero=["HHH","Under Taker","Shown Mical","Batista","Stone Gold"]
# idx= 0
# index=0
# # while idx < len(Hero):
# #     print(Hero[idx])
# #     idx= idx+1
# while index < len(list):
#     print(list[index])
#     index= index+1 

# For tuple print. 
# tuple=(1,4,9,16,25,36,49,64,81,100)
# i=0
# while i < len(tuple):
#     print(tuple[i])
#     i=i+1

# For find a number and its index postion in list and tuple.
# t = (1,4,9,16,25,36,49,16,64,81,100,16,16,)
# x = 49
# i = 0
# while i < len(t):
#     if (t[i]==x):
#         print("Match:-", i)
#     i+=1
# while i < len(values):
#     if (values[i]==x):
#          print("Match:-", i)
#     i+=1
# 2nd ways
# for i in tup: 
#     if i==x:      
#       print("Match:  ",tup.index(i))


# t = (1,4,9,16,25,36,49,16,64,81,100,16,16,)
# x = 16
# i = 0
# while i < len(t):
#     if (t[i]==x):
#         print("Match:-", i)
#     i+=1
# count=t.count(x)    
# print(count)


# t = (1,4,9,16,25,36,49,16,64,81,100,16,16,)
# x = 44
# i = 0
# while i< len(t):
#     if (t[i]==x):
#         print("Found on index:-",i)
#     else:
#         print("Finding")
#     i=i+1 
# count=t.count(x)
# print(count)

# Break and continue example.

# i = 1
# while i <= 10:
#     print (i)
#     if (i==7):
#         break
#     i=i+1

# continue is the break a letter, Word and character.
# i = 0
# while i <= 10:
#     if (i==7):
#         i=i+1
#         continue
#     print(i)
#     i=i+1
# #print("end of loop")

# Print only even or Odd number in to counting.(For Odd NumberS)
 
## For Loop -- its worked on secquencly woring on progarams as like \:- string, list, tuple ect.

# l9o

# Furits=['mango','apple','banana','graps','cheeku','orange']
# for name in Furits:
#     print(name)

# list=(1,2,3,4,5)
# for value in list:
#     print(value)

# Furits=('mango','apple','banana','graps','cheeku','orange')
# for name in Furits:
#     print(name)

## How to print string character.
# str="SARVESHWAR"
# for char in str:
#     print(char)

## HOW to any work and print after runned loop.
# str="SARVESHWAR"
# for char in str:
#     print(char)
# else:
#     print("SARVESHWAR")
    




# print(range(5))


# big way to print in sequence.
# seq=range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])

# New way to print sequence.
# sets
# collection = {1,2,3,4}
# print(collection)
# print(type(collection))

# # print 500 times numbering.
# i=1
# while i <=500:
#     print("Numbring Name",i)
#     i=i+1

# print i 5 times.
# i=1
# while i<=5:
#     print(i)
#     i=i+1
# print("The End of conting")

# Revers counting
# i=5
# while i>=1:
#     print(i)
#     i=i-1

# Question 1 -- print number from 1 to 100.
# i=1
# while i<=100:
#     print(i)
#     i=i+1

# Question 2 -- print number from 100 to 1.
# i=100  
# while i >=1:
#     print(i)
#     i=i-1

# Question 3 -- print number from 100 to 1.    
# i=1
# while i <= 10:
#     print(350*i)
#     i=i+1
# print("Table Completed")

# print table with user input.
# i=1
# n=int(input("Enter Number:-"))
# while i <=10 :
#     print(i*n)
#     i=i+1

# Question 4 -- print the elements of follwoing list using a loop.
# list=[1,5,8,6,16,49,78,81,96,101,240,160,850.7001]
# idx=0
# while idx < len(list):
#     print(list[idx])
#     idx=idx+1

# # Revers this above
# list=[1,5,8,6,16,49,78,81,96,101,240,160,850.7001]
# idx=len(list)-1
# while idx > 0:
#     print(list[idx])
#     idx=idx-1

# list=[8,88,888,8888,88888,888888]
# idx=0
# while idx < len(list):
#     print(list[idx])
#     idx=idx+1

# # Revers this above
# list=[8,88,888,8888,88888,888888]
# idx=len(list)-1
# while idx > 0:
#     print(list[idx])
#     idx=idx-1        