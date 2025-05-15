# info = { 
#     "key" : "Value, this is value of key",
#     "name" : "Sarvesh",
#     "learning" : "chapter 4"
# }
# print(info)
#{'key': 'Value, this is value of key', 'name': 'Sarvesh', 'learning': 'chapter 4'}

#Add Floting value and intger
# info = { 
#     "key" : "Value, this is value of key",
#     "name" : "Sarvesh",
#     "learning" : "chapter 4",
#     "Marks" : 44.8,
#     "Age": 21,
#     "Is Adult" : False,
#     "Is PAN":"Yes" 
#     }
#print(info)
#{'key': 'Value, this is value of key', 'name': 'Sarvesh', 'learning': 'chapter 4', 'Marks': 44.8, 'Age': 21, 'Is Adult': False, 'Is PAN': 'Yes'}


#How to add list and Tuple in dictionary
# info = { 
#     "key" : "Value, this is value of key",
#     "name" :"sarvesh",
#     "Subject-lsit" : ["math","english","science"],
#     "Topic-Tup": ("String","list&Tup"),
#     "Marks" : 44.6,
#     "Age": 21,
#     "Is Adult" : False,
#     }
# print(type(info))
#<class 'dict'>
# print(info)
#{'key': 'Value, this is value of key', 'name': 'sarvesh', 'Subject-lsit': ['math', 'english', 'science'], 'Topic-Tup': ('String', 'list&Tup'), 'Marks': 44.6, 'Age': 21, 'Is Adult': False}

#how to print only value not key from dictionary
# dict = { 
#      "key" : "Value, this is value of key",  
#      "name" :"sarvesh",
#      "Subject-lsit" : ["math","english","science"],
#      "Topic-Tup": ("String","list&Tup"),
#      "Marks" : 44.6,
#      "Age": 21,
#      "Is Adult" : False,
#      }
# print(dict.keys())
# print(dict.values())
# print(dict.items())

# print(dict["Subject-lsit"])
# print(dict["name"])
# print(dict["key"], dict["name"])

# how to change key value and print
# info = { 
#     "name":"Sarvesh"
#  }   
# info["name"]="Sarveshwar Kumar"
# print(info)

# how to add comma in between of 1 word.
# info ={
#   "name": "Sarveshwar Kumar"
# }
# # Split the name into first and last parts
# name_parts = info["name"].split()
# # Join with a comma
# print(", ".join(name_parts))
# Print hoga + Sarveshwar, Kumar😊

# how to value change and print with last value.
# info = { 
#      "name":"Sarvesh"
#  }   
# info["name"]="Sarveshwar Kumar"
# info["name"]="Rishi Yadav"
# info["name"]="Pankaj"
# print(info)
#print hoga == jo last m hai as {'name': 'Pankaj'}

# Nested Dictionary (create 1 dictionary in dicitionary)
# students={
#     'student1':{
#         'name': 'Vishal',
#         'class': 10,
#         'subject': ['History','Science'] 
#     }
# }
# #students['student1'] ['class']= "MBBS"
# print(students['student1']['class']) 

# how to crate (create 2 dictionary in dicitionary) and print.
# students={
#     'student1':{
#         'name': 'Raj Kumar',
#         'class': '12th',
#         'subject': ['History',' English', 'Drawing']
#     },   
#     'student2':{
#         'name': 'Ram Kumar',
#         'class': '12th',
#         'subject': ['Math', 'English', 'Hindi']
#     } 
# }
# print(students['student1'],students['student2'])
# # print(students['student1'])
# # print(students['student2'])


# How to change key value in dictionary when dictionary is creted on another dictionary. 
# school={
#     'class1': {
#         'Student1': 'Manish',
#         'roll no': '01',
#         'Subject' : ["hindi", 'English']
#     },
#     'class2': {
#         'Student2': 'Rahul Malhotra',
#         'roll no': '09',
#         'Subject' : ["hindi", 'English']
#     }        
#     }
# school['class1']['Student1']='Rajev Bajaj'
# print(school['class1'])

# How to add NUll dictionary
# null_dict={}
# print(null_dict)
# PH--{}

# How to add value in NUll Dictionary
# null_dict={}
# null_dict['name']= 'Sarvesh'
# print(null_dict)
# PH--{'name': 'Sarvesh'}

# how to print nexted dictionary value.
# school={
#      'class1': {
#          'Student1': 'Manish',
#          'rollNo': '01',
#          'Subject' : ("hindi", 'English')
#      }
# }
# print(school["class1"]["Subject"])
# # PH--('hindi', 'English')

# # If print subject English
# school={
#      'class1': {
#          'Student1': 'Manish',
#          'rollNo': '01',
#          'Subject' : ["hindi", 'English']
#      }
# }
# print(school["class1"]["Subject"][1])
# PH-- English


# how to print all keys in 1 method dictionary keys.
# school={'student1': 'Manish',
#         'student2': 'Rakesh',
#         'student3': 'Mohit',
#     'class1': {  
#      'student1 roll no': 0.1,
#      'student2 roll no': '02',
#      'student3 roll no': '03',
#      'class2':{
#          'student1 Subject' : ["hindi", 'English'],
#          'student2 Subject' : ["Math", 'science'],
#          'student3 Subject' : ["SST", 'Drawing'],
#      }   
#   }
# }
# print(school.keys())

# How to print nexted dictionary keys jb vo kisi main dictionary ke ander ho.
# school={'student1': 'Manish',
#         'student2': 'Rakesh',
#         'student3': 'Mohit',
#     'class1': {  
#      'student1 roll no': 0.1,
#      'student2 roll no': '02',
#      'student3 roll no': '03',
#     'class2': {
#         'student1 Subject' : ["hindi", 'English'],
#         'student2 Subject' : ["Math", 'science'],
#         'student3 Subject' : ["SST", 'Drawing'],
#      }   
#   }
# }
# print(school.keys())
# print(school['class1'].keys())
# print(school['class1']['class2'].keys())

# if you want to print only keys in list format.
# school={'student1': 'Manish',
#         'student2': 'Rakesh',
#         'student3': 'Mohit',
#     'class1': {  
#      'student1 roll no': 0.1,
#      'student2 roll no': '02',
#      'student3 roll no': '03',
#     'class2': {
#          'student1 Subject' : ["hindi", 'English'],
#          'student2 Subject' : ["Math", 'science'],
#          'student3 Subject' : ["SST", 'Drawing'],
#      }   
#   }
# }
# print(list(school['class1']['class2'].keys()))
# print(tuple(school['class1']['class2'].keys()))
# class1_values = school['class1'].values()
# print(class1_values)
# print(type(school))


# print(school.values())
# print(school['class1'].values())
# print(school['class1']['class2'].values())

# print(list(school.values()))
# print(list(school['class1'].values()))
# print(list(school['class1']['class2'].values()))

# print(tuple(school.values()))
# print(tuple(school['class1'].values()))
# print(tuple(school['class1']['class2'].values()))

# print(len(list(school.values())))
# print(len(list(school['class1'].values())))
# print(len(list(school['class1']['class2'].values())))

# How to print only total keys of nexted dictionary.
# print(list(school['çlass1']['class2'].keys()))

# school={'student1': 'Manish',
#         'student2': 'Rakesh',
#         'student3': 'Mohit',
#     'class1': {  
#      'student1 roll no': 0.1,
#      'student2 roll no': '02',
#      'student3 roll no': '03',
#     },
#       'class2': {
#          'student1 Subject' : ["hindi", 'English'],
#          'student2 Subject' : ["Math", 'science'],
#           'student3 Subject' : ["SST", 'Drawing'],
#      }   
  
# }
# print(school.items())
# print(school['class1'].items())
# print(school['class1']['class2'].items())

# print(list(school.values()))
# print(list(school['class1'].items()))
# print(list(school['class1']['class2'].items()))

# print(len(list(school.items())))
# print(len(list(school['class1'].items())))
# print(len(list(school['class1']['class2'].items())))
# print(school['class1'].values)
# print(school['class2'].values())   


# how to change subject is nexted dictironary 
# school={'student1': 'Manish',
#         'student2': 'Rakesh',
#         'student3': 'Mohit',
#     'class1': {  
#      'student1 roll no': 0.1,
#      'student2 roll no': '02',
#      'student3 roll no': '03',
#     },
#       'class2': {
#          'student1 Subject' : ["hindi", 'English'],
#          'student2 Subject' : ["Math", 'science'],
#           'student3 Subject' : ["SST", 'Drawing'],
#      }   
#  }
# school['class2']['student2 Subject'][0]="english"
# print(school["class2"].values())
# school['class1']['Student1']='Rajev Bajaj'
# print(school['class1'])
# print(len(school.keys()))
# print(len(school['class1'].keys()))
# print(len(school['class2'].keys()))


# How to print all items.
# school={'student1': 'Manish',
#         'student2': 'Rakesh',
#         'student3': 'Mohit',
#     'class1': {  
#      'student1 roll no': 0.1,
#      'student2 roll no': '02',
#      'student3 roll no': '03',
#     },
#       'class2': {
#          'student1 Subject' : ["hindi", 'English'],
#          'student2 Subject' : ["Math", 'science'],
#           'student3 Subject' : ["SST", 'Drawing'],
#      }   
#  }
# print(list(school.items()))

# How to print individually tuple.
# school={'student1': 'Manish',
#         'student2': 'Rakesh',
#         'student3': 'Mohit',
#     'class1': {  
#      'student1 roll no': 0.1,
#      'student2 roll no': '02',
#      'student3 roll no': '03',
#     },
#       'class2': {
#          'student1 Subject' : ["hindi", 'English'],
#          'student2 Subject' : ["Math", 'science'],
#           'student3 Subject' : ["SST", 'Drawing'],
#      }   
#  }

# printtuple = list(school.items())
# print(printtuple[0])
# school={
#     'class1':{
#       'teacher':'anjli'
#        },
#     'students':{
#       'student1': 'Manish',
#       'student2': 'Rakesh',
#       'student3': 'Mohit'
#     },
#     'subjects':{
#       'student1': ['Englist','Hindi'],
#       'student2': ['Math','Scienc'],
#       'student3': ['Histry','Panting']
#     }, 
#   }

# #print(school)
# print(school["class1"])
# print(school["students"]['student1'])
# print(school['subjects'])
# print(school['subjects']['student1'])
# school['subjects']['student1'] == "Ramayan","Mahabhrat"
# print(school['subjects']['student1'][1])


# school={
#     'class1':{
#       'teacher':'anjli'
#        },
#     'students':{
#       'student1': 'Manish',
#       'student2': 'Rakesh',
#       'student3': 'Mohit'
#     },
#       'subjects':{
#       'student1': 'Englist'',''Hindi',
#       'student2': 'Math'',''Scienc',
#       'student3': 'Histry'',''Panting'
#     }, 
#   }
#print(school.items())
#Type casting
#print(list(school)) # how to check how many nexted dictionary in a main distionary.

# yy=list(school) #2nd way -- how to check how many nexted dictionary in a main distionary.
# print(yy)

# school={
#     'Addmission': "open",
#     'class1':{
#       'teacher':'anjli'
#        },
#     'students':{
#       'student1': 'Manish',
#       'student2': 'Rakesh',
#       'student3': 'Mohit'
#   },
#     'subjects':{
#       'student1': 'Englist'',''Hindi',
#       'student2': 'Math'',''Scienc',
#       'student3': 'Histry'',''Panting'
#     }, 
#   }
# admit = list(school.items()) #  how to print all dictionaryes values one by one with variable.
# #print(admit)
# print(admit[0])
# print(admit[1])
# print(admit[2])
# print(admit[3])
# PH:- ('Addmission', 'open')
# ('class1', {'teacher': 'anjli'})
# ('students', {'student1': 'Manish', 'student2': 'Rakesh', 'student3': 'Mohit'})
# ('subjects', {'student1': 'Englist,Hindi', 'student2': 'Math,Scienc', 'student3': 'Histry,Panting'})


# school={
#     'Addmission': "open",
#     'Addmission1': "close",
#     'class1':{
#       'teacher':'anjli'
#        },
#     'students':{
#       'student1': 'Manish',
#       'student2': 'Rakesh',
#       'student3': 'Mohit'
#   },
#     'subjects':{
#       'student1': 'Englist'',''Hindi',
#       'student2': 'Math'',''Scienc',
#       'student3': 'Histry'',''Panting'
#     }, 
#   }
# print(school['Addmission'])
# print(school['class1'])
# print(school['students'])
# print(school['subjects'])
# How to print 1 key value in the nexted dictionary.
#print(school['subjects']['student2'][1])  #print only science for list 
# How to print nexted dictionary keys and values.
#print(school['class1'])                   #PH --{'teacher': 'anjli'}
# How to print nexted dictionary only keys and values.
#print(school.keys())                      #PH--dict_keys(['Addmission', 'Addmission1', 'class1', 'students', 'subjects'])
# How to print main dictionary only values.
#print(school['subjects'].values())        #PH-dict_values(['Englist,Hindi', 'Math,Science', 'Histry,Panting'])
# How to print nexted dictionary only keys.
#print(school['subjects'].keys())          #PH-dict_keys(['student1', 'student2', 'student3'])
# How many pairs in main and nexted dictionary.
#print(school['subjects'].items())         #PH-dict_items([('student1', 'Englist,Hindi'), ('student2', 'Math,Science'), ('student3', 'Histry,Panting')])




# Mydict.get

# How to get key value from method.
# school={
#     'Addmission': "open",
#     'Addmission1': "close",
#     'class1':{
#       'teacher':'anjli'
#        },
#       }
# print(school["Addmission1"])         # (1)
# print(school.get("Addmission1"))     # (2)
# print("hello") 
# PH- close,close,hello but if condition 1 key value is wrong then it will print an error. if condition 2 then it will be print None.

# mydict.update For add new nexted dictionary and main dictionary.
# school={
#     'Addmission': "open",
#     'Addmission1': "close",
#     'class1':{
#       'teacher':'anjli'
#        },
#       }
#school.update({'Addmission3':'timeing'}) # for add new dictionary in main dictionary.
# print(school)
#print(list(school)) for check it is added or not.

# school['class1'].update({'Addmission3':'timeing'}) # for add new dictionary in nexted dictionary.
# print(school['class1'].keys())

# how to add multiple Dictionary in main and nexted dictionary.
# school={
#     'Addmission': "open",
#     'Addmission1': "close",
#     'class1':{
#       'teacher':'Anjli'
#        },
#       }
# school['class1'].update({'teacher1':'Rahul' ,'teacher2':'Manoj'})
# #school.update({'teacher1':'Rahul' ,'teacher2':'Manoj'})
# print(school)
# print(school['class1'])

#how to change key value in main and nexted dictionary. if we gives key name same and value is change then overide on key value.
# 

#      Set Methods
# How to print sets.
# sets ={1,2,3,4}
# print(sets)
# print(type(sets))
# PH--{1, 2, 3, 4}
# <class 'set'>

# Add String in sets
# sets={1,2,3,4,4,4,4,4, "brother","hello", "brother" }   # duplicate value will be skiped.
# print(sets)
# PH--{1, 2, 3, 4, 'brother', 'hello'}   # unorderd print.

# Check length in sets
# sets={1,2,3,4,4,4,4,4, "brother","hello", "brother" }
# print(len(sets))
# PH-- 6

#Create Empty set. (set())
# empty_set = set()   
# print(empty_set)
# Ph--set()

# Add value in empty set. (.add(element))
# empty_set = set()   
# empty_set.add(1) #integer
# empty_set.add(2)
# empty_set.add(2)  # again value 2 (duplicate value will be ignor.)
# print(empty_set)
# PH-- {1, 2}

# Remove value (.remove(element))
# empty_set = set()   
# empty_set.add(1) #integer
# empty_set.add(2)
# empty_set.add(2)  # again value 2 (duplicate value will be ignor.)
# empty_set.remove(2)
# print(empty_set)
# #PH-- {1}

# # if removed vaule is not exists in set.
# empty_set = set()   
# empty_set.add(1) #integer
# empty_set.add(2)
# empty_set.add(2)  # again value 2 (duplicate value will be ignor.)
# empty_set.remove(102)
# print(empty_set)
#PH-- Error

# student=set()
# student.add("1.student-Manoj")
# student.add("2.student-Parmod")
# student.add("3.student-Kishor")
# print(student)
# PH--{'3.student-Kishor', '2.student-Parmod', '1.student-Manoj'}

# For add multipale numbers in one line.
# number={1,2,3,4}
# number.add(100)                                  # for single value add
# number.update([200,300,400])                     # for add multiple value add.
# print(number)

# when we add in list then unhasable type -- List error throug


# Print all values and length.
# collection=set()
# collection.add(1)
# collection.add(2)
# collection.add("Sarvesh")
# collection.add(4.65)
# #collection.add('test','fast')  wrong way
# collection.add('test')
# collection.add('fast')
# print(collection)
# print(len(collection))

# For clear all values (.clear())
# collection=set()
# collection.add(1)
# collection.add(2)
# collection.add("Sarvesh")
# collection.add(4.65)
# #collection.add('test','fast')  wrong way
# collection.add('test')
# collection.add('fast')
# collection.clear()
# print(collection)
# print(len(collection))

# For clear rendom values. (.pop())
# collection=set()
# collection.add(21)
# collection.add(25)
# collection.add("Sarvesh")
# collection.add("Sarvesh")
# collection.add(20.65)
# #collection.add('test','fast')  wrong way
# collection.add('that')
# collection.add('fast')
# collection.pop()
# print(collection)
# print(len(collection))

# add 2 sets with unique values. (.union(set2))
# set1={2,4,6,8,10,11}
# set2={1,3,4,6,7,9,10}
# uniqe_values=set1.intersection(set2)
# print("uniqe values=",uniqe_values)


# set1={2,9,5,8,1}
# set2={2,4,5,12,}
# popp=set1.pop()
# print(popp)
# print(set1)
#print(set1.remove(0))

# Difference show in set1 and set2 and retur unique value which is not exists in set2. Wiseversa.
# set1={2,9,5,8,1}
# set2={2,4,5,12,}
# diff=set1.difference(set2) # 8 1 9
# diff=set2.difference(set1) # 12 4
# print(diff)

# For update valuse add new values in main set duplicate value will be removed.
# set1={2,9,5,8,1}
# set2={2,4,5,12,}
# update=set1.update(set2) # 8 1 9
# print(update)



# a=31
# b=30
# #print(a>b)
# print(a>b and a==b)


# Dict={
#      '0': 'Daily',
#      '1':'Weekly'
# }
# Dict1={
#      '3': 'Continously',
#      '4':'Monthly'
# }
# key = 5
# if str(key) in Dict1:
#     print(Dict1[str(key)])
# else:
#     print("0")

# Dict1.update({'5':"Custom"})
# print(Dict1)
 