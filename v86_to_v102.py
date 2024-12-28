"""zip function,Image Manipulation With Pillow,Doc String & Commenting,Errors And Exceptions Raising(try and except),Regular Expressions         """

# # v86:zip function (built in function)             #zip : making aloop on more than one iterator
# # Practical => Loop on Many Iterators With Zip() 
# # zip() Return A Zip Object Contains All Objects
# # zip() Length Is The Length of Lowest Object

# mylist1=['ali','ahmed']
# mylist2=[2,4,6,7]
# mytuple=('a','b','c')
# mydic={'s1':1,'s2':2}
# for rec1,rec2,rec3,rec4 in zip(mylist1,mylist2,mytuple,mydic) :
#     print(f'{rec2}-{rec3}=>{rec1},{rec4}:{mydic[rec4]}')
    
    
# # v87:Image Manipulation With Pillow            :controll in picture
# https://pillow.readthedocs.io/en/stable/reference/Image.html
# from PIL import Image    
# myimage=Image.open("/home/ali/Downloads/IMG_0514 (1).jpeg")
# # myimage.show()   
# mybox=(20, 20, 500, 500)

#     # Here the image "im" is cropped and assigned to new variable im_crop
# im_crop = myimage.crop(mybox)    
# # im_crop.show()  
# convertimage = myimage.convert("L")  
# # convertimage.show()

# # v88 :Doc String & Commenting vs Documenting --
# # [1] Documentation String For Class, Module or Function
# # [2] Can Be Accessed From The Help and Doc Attributes
# # [3] Made For Understanding The Functionality of The Complex Code
# # [4] Theres One Line and Multiple Line Doc Strings
# def calculate_nums(n1,n2):
#     """definition : this function to calculate numbers
#        parameters : n1,n2
#        return :sum of numbers"""          #this is a comment to doc string
#     print(n1+n2)
    
# # print(calculate_nums.__doc__)
# # help(calculate_nums)

# # v89: Installing And Use Pylint For Better Code 
# # pip install pylint                              #to make your code clean and on best pracrtice
# """
# This is My Module
# To Create Function
# To Say Hello
# """

# def say_hello(name):
#   '''This Function Only Say Hello To Someone'''
#   msg = "Hello"
#   return f"{msg} {name}"

# say_hello("Ahmed")

# # assignment 19
# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []
# final_string=""
# for data in zip(my_list, my_tuple):
#     for n in data:
#         final_string +=f"{n.lower()}"
# print(final_string.capitalize()) 


##########################################################################################################################
# # v90: Errors And Exceptions Raising 
# # [1] Exceptions Is A Runtime Error Reporting Mechanism
# # [2] Exception Gives You The Message To Understand The Problem
# # [3] Traceback Gives You The Line To Look For The Code in This Line
# # [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# # [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# # [6] raise Keyword Used To Raise Your Own Exceptions

# def check(a) -> int:
#     if a >35 :
#         raise ValueError("please add number less than 35")
# # check(50)

# try:                     #write condition if true the function continue else make exception
#     check("50")
#     # print(28/0)
    
# except ValueError:       #exception is used when errors happen can choose specific error or not
#     print("please add number less than 35")

# except ZeroDivisionError:
#     print("please add number more than 0")
# except:                  #to any other errors
#     print("errors happen")
# else :                   #when errors not happen  and almost not used
#     print("no errors")
# finally :                # it is working errors happened or not
#     print("The Process done")

# # # v92:  Exceptions Handling    
# # the_file = None
# # the_tries = 5

# # while the_tries > 0:
# #   try:  # Try To Open The File
# #     print("Enter The File Name With Absolute Path To Open")
# #     print(f"You Have {the_tries} Tries Left")
# #     print("Example: D:\Python\Files\yourfile.extension")
# #     file_name_and_path = input("File Name => : ").strip()
# #     the_file = open(file_name_and_path, 'r')
# #     print(the_file.read())
# #     break
# #   except FileNotFoundError:
# #     print("File Not Found Please Be Sure The Name is Valid")
# #     the_tries -= 1
# #   except:
# #     print("Error Happen")
# #   finally:
# #     if the_file is not None:
# #       the_file.close()
# #       print("File Closed.")

# # else:
# #   print("All Tries Is Done")

# # v94:hinting                              #-> to add definition to func
# def check(a) -> int:
#     if a >35 :
#         print("please add number less than 35")
# check(50)

# # assign20
# LETTER = input("Add Letter From A to Z ")

# try :
#     if len(LETTER)>1 :
#          raise IndexError
#     elif LETTER != LETTER.capitalize():
#          raise  ValueError
       
# except IndexError: 
#     print("You Must Write One Character Only")
# except ValueError:
#     print("The Letter Not In A - Z")
# else :
#     print(f"You Typed {LETTER}")

# def calculate(num1, num2) -> int:
#   return num1 + num2

# print(calculate(20, 30))

########################################################################################################################

# v100: Regular Expressions => Re Module Search And FindAll --
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)

import re
mysearch=re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)","ali@gmail.com")
print(mysearch)
print(mysearch.span())
print(mysearch.string)
print(mysearch.group())

youremail=input("please add your email :")
email_list=[]
search=re.findall(r"^[A-z0-9\.]+@[A-z0-9]+\.com|net$",youremail)
if search !=[]:
    email_list.append(search)
    print ("Added email")
else :
    print ("Not valid email")
for email in email_list :
    print (email)

# v101: Regular Expressions => Re Module Split And Sub 
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Splitted On Each Match
# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want

import re 
mystring="ali mohamed mahoud"
mysplit=re.split(r'\s',mystring,2)
print (mysplit)
print (re.sub(r'\s',r"-",mystring,1))

# v102: Regular Expressions
import re 
mystring="ali mohamed mahoud \n i am an Engineer"
mysearch=re.search(r"(\sm)?(\sa)",mystring,re.M)
print (mysearch)
# print (mysearch.group(1))
# print (mysearch.groups())                        #get error if not found





