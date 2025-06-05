# For crete a file.
# f = open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Sarvesh\Demo.txt","rt")
# data = f.read()
# print(data)
# print(type(data))
# f. close()

# # For read line of characters. 10 characters
# f = open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Sarvesh\Demo.txt","r")
# data = f.read(10)
# print(data)
# f. close()

# # For read one line at a time for help of list. use f.readlines()
# f = open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Sarvesh\Demo.txt","r")
# line3 = f.readlines()
# print(line3[2])
# #print(line3)
# f. close()  

# print first and second and third line.
# f = open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Sarvesh\Demo.txt","r")

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3) 
# f. close() 

# Space print hoga if we read first and liens print 2 me.
# f = open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Sarvesh\Demo.txt","r")
# data = f.read()
# print(data)

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f. close() 

# File open in write mode.
# f = open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Sarvesh\Demo.txt","w")
# f.write("previous write data will removed and new line is added.")
# f. close() 

# # if data write with double cots ""
# f = open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Sarvesh\Demo.txt","w")
# f.write("previous write data will removed and new line happy birth day is added.")
# f. close()

# for add data in last.
# f = open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Sarvesh\Demo.txt","a")
# f.write("new date is addddded line. this is testing for added new line.")
# f. close()

# Data move in next line.
# f = open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Sarvesh\Demo.txt","w+")
# f.write("previous write data will removed and new line happy birth day is added.\nnew date is addddded line. \nthis is testing for added new line.")
# f. close()

# without create (new file is added in your folder.) for "w" and "a"

# f=open("Rajesh.txt","a")
# f.close()

# use of r+ (data overwrite from starting.)
# f=open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Sarvesh\Demo.txt","r+")
# f.write("\nMy name is - Sarveshwar kumar")
# print(f.read())
# f.close()

# use of w+ (read and write)
# f=open(r"C:\Users\Sarveshwar Kumar\Desktop\Sarvesh\python\python-project\Sarvesh\Demo.txt","w+")
# f.write("My name is - Sarveshwar kumar\nThis is for testing purpuse.")
# print(f.read())
# f.close()

# use code with syntax.(show old data on terminal and new data is appearing in file. )
# with open ("NEW FILE.TXT","r") as f:
#     data=f.read()
#     print(data)
# with open("NEW FILE.TXT","w") as f:
#     f.write ("My name is sarveshwar Kumar. (Test Engineer)")

# for delete a file. (import os) create and delete
# # f=open("Rajesh.txt","a")
# # f.close()

# import os
# os.remove("rajesh.txt")

# f=open("Rajesh.txt","a")
# f.close()
 
# Question 1-- Crete a new file and add data in it through python?
# f=open("NEWFILEANDFOLDER.txt","w")
# f.write("My name is sarvehwar kumar sharma & Rock007")
# f.close()

f=open("Acorp.py","w")
f.write("Stating of coding with python.")
f.close()   


