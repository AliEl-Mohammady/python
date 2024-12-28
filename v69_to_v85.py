
                # Built in function , Built in module ,Date and datetime ,generator and Decorator 

# v69:built in function 
x =[1,5,8,6]
y =[1,5,False,6]
if all(y):                            #all() :check if all items of iterable element is true
    print("All elements is true ")
else:
    print("At least one element is False ")
    
if any (x):                            #any() :check if one item of  iterable element is true
    print("At least one element is True ")
else:
    print("All element is False ")
x=10
print(bin(x))                          #bin() :get binary number of variable
print(id(x))                           #id() :get id number of variable

# v70:built in function p2
x =[1,5,8,6]
print(sum(x,100))                       #Sum(iterable,start) :get sum of numbers of iterable variable and add numbers to it
print(round(100.55555555,2))            #round(number,numdigits) :get digits of numbers
print(list(range(10,100,10)))           #range(number,number,step) :get list of numbers
print("Eng","Ali",sep="@",end=" ")      #print("text",sep:by default it 's space,end:by default it 's \n) 
print("mohamed",sep="@") 
print("mahoud",sep="@") 

# v71:built in function p3
x =[1,5,8,6]
print(abs(-100))                       #Abs(number) :get positive value  of numbers 
print(pow(10,2,3))                     #Pow(number,exponent,division) :get rest value  of numbers after division
print(min(x))                          #Min(items or list) :get min value  of numbers 
print(min("a","c","d"))                     
print(max(x))                          #Max(items or list) :get max value  of numbers 
print(x[slice(2,5,2)])                 #slice(start ,end ,step) :get slice

# assignment15
values = (0, 1, 2)

if any(values):

  my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

  print("Good")

else:

  print("Bad")

#"Good"
v =40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

def my_all(Iterable):
    if type(Iterable)==list or type(Iterable)==tuple :
        for line in Iterable :
            if bool(line)!=False :
                v=True
            else :
                v=False
                break
        print(v)
my_all([1,None,5])
my_all((1,2,[]))

def my_any(Iterable):
    if type(Iterable)==list or type(Iterable)==tuple :
        for line in Iterable :
            if bool(line)==False :
                v=False
            else :
                v=True
                break
        print(v)
    else:
        pass
my_any([[],None,()])
my_any((1,2,[]))

def my_min(Iterable):
    if type(Iterable)==list or type(Iterable)==tuple :
        x=0
        for line in Iterable :
            if line < x :
                x=line
            else :
                x=x
        print(x)
print("x"*40)       


# v72:map(fun ,iterable) :making aloop
def formattext(text):
    return text
    
formattext([1,2,3])
print(map(formattext,[1,2,3]))
print(list(map(formattext,[1,2,3])))
for name in map(formattext,[1,2,3]):
    print(name)
for name in map(lambda x :x,[1,2,3]):
    print(name)
print("x"*40)

# v73:filter(fun ,iterable) :making check condition
def checktext(text):
    return text.startswith('a')
    
myNames=['ahmed','amr','ola']
print(filter(checktext,[1,2,3]))
filtername=filter(checktext,myNames)
for name in filtername:
    print(name)
for name in filter(lambda x :x.startswith('a'),myNames):
    print(name)
print("x"*40)

# v74:reduce(fun ,iterable) :making acondition on first 2 items then on next and continue
from functools import reduce
def sumnumber(num1,num2):
    return num1+num2
    
myNums=[1,2,5,8,9]
print(reduce(sumnumber,myNums))
reducenums=reduce(sumnumber,myNums)
print(reducenums)
reducenums=reduce(lambda x1,x2 :x1+x2,myNums)
print(reducenums)

# v75:enumerate ,help,reversed
myfriend=['ali','ahmed']
for rec in enumerate(myfriend):                 #enumerate(iterable=,start of counter) :making counter for loop
    print(rec)
for num,friend in enumerate(myfriend,10):
    print(f'{num}-->{friend}')

for rec in enumerate(reversed(myfriend)):       #reversed(iterable=) :making reverse for loop
    print(rec)

# print(help(reversed))                           #help(functions) :get information about func

# assignment16
def remove_chars(text):
    return text[1:-1]
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

for name in map(remove_chars,friends_map):
    print(name)   
# Output
"Eman"
"Ahmed"
"Sameh"
"Osama"
    
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
def get_name(text):
    return text.endswith('m')
names=filter(get_name,friends_filter)
for name in names:
    print(name) 
# Output
"Wessam"
"Essam"

nums = [2, 4, 6, 2]
from functools import reduce
def sumnumber(num1,num2):
    return num1*num2
    
reducenums=reduce(sumnumber,nums)
print(reducenums)
# Output
96

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
for c,s in enumerate(reversed(skills),50) :
    if type(s)==int :
        continue
    else :
        print(f"{c} - {s}")
# Output
"50 - JavaScript"
"52 - Python"
"53 - PHP"
"55 - CSS"
"56 - HTML"

##############################################################################################################
# v76:built in module
import random                                      #import module_name :to get module 
print(dir(random))                                 #dir (module_name)  :to know all function inside this module
from random import randint,randrange               #from module_name import functions or *(stres)
from datetime import *
print(randrange(10,20))
print("x"*40)

# v77:create module
import sys 
print(sys)
print(dir(sys))
print(sys.path)
# import v56_to_v68 as ali                          # we can import any of my module and use it's function 
import v56_to_v68 as ali                            #we can use alias after as 
print(dir(ali))                                   
mylist={'math':10,'science':20}
ali.get_the_scores("ali",**mylist)

# v78:module and package
# package consist of modules
# Modules List "https://docs.python.org/3/py-modindex.html"
# Packages and Modules Directory "https://pypi.org/"
# pip --version : to know version of pip
# pip list :to know all module in pip
# pip install --upgrade pip :to upgrade modules
# pip install  package :to install package 
import pyfiglet,termcolor
print(termcolor.colored(pyfiglet.figlet_format("ALI"),'red'))

# assignment16
import random
# print(dir(random))
print(f"Random Number Between 10 And 50 => {random.randint(10, 50)}")

print("Random Even Number Between 2 And 10 => %s" % random.randrange(2, 10,step=2))
print("Random Odd Number Between 1 And 9 => {:.2f}".format(random.randrange(1, 9,step=2)))

######################################################################################################################
# v79 : date and datetime
import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(dir(datetime.datetime.now()))
print(datetime.datetime.now().time())
print(datetime.datetime.now().hour)
print(datetime.datetime.now().time().second)
print(datetime.datetime.now().second)
print(datetime.datetime.now().today())
print(datetime.date.today())

# v80 :format date and time
#  https://strftime.org/
mybirthday=datetime.datetime(2000,4,7)
print(mybirthday)
print(mybirthday.strftime("%A %B %Y"))
print(mybirthday.strftime("%-d %-m %Y"))
print(mybirthday.strftime("%d %m %Y"))

#######################################################################################################################
# v81 :iterable and iterator 
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element

myname='Ali'
iterator=iter(myname)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))                 #StopIteration

#v82: Generators 

# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control

def generator():
    yield 2
    yield 5
    yield 6
    yield 7
  
mygen=generator()  
print(next(mygen))
print(next(mygen))
for rec in mygen :
    print(rec)

# v83:decorator
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
def mydecorator(func):                      #decorator func
    def handle_decorator():                 #any name
        print('hello')
        func()                 
        print(',be brave')
    
    return handle_decorator

@mydecorator                                 #call deecorator
def full_name():
    print('Ali Mohamed')
    
full_name()


# v84:decorator
def mydecoratorcalc(func):                   #decorator func
    def handle_decorator(num1,num2):         #any name function when using paramters
        if num1 <0 or num2 < 0 :
            print('negative number')
        func(num1,num2)                     
    return handle_decorator

def mydecoratorafrer(func):             
    def nestedfunc(num1,num2):
        func(num1,num2)
        print(',be attention')
    return nestedfunc

@mydecoratorcalc                           #call more than decotator   
@mydecoratorafrer    
def calculate(n1,n2):
    print(n1+n2)
calculate(-10,20)

# v85:speedtest
from time import time

def myDecorator(func):  # Decorator
  def nestedFunc(*numbers):  # Any Name Its Just For Decoration
    for number in numbers:
      if number < 0:
        print("Beware One Of The Numbers Is Less Than Zero")
    func(*numbers)  # Execute Function
  return nestedFunc  # Return All Data

@myDecorator
def calculate(n1, n2, n3, n4):
  print(n1 + n2 + n3 + n4)
calculate(-5, 90, 50, 150)


def speedTest(func):
  def wrapper():
    start = time()
    func()
    end = time()
    print(f"Function Running Time Is: {end - start}")
  return wrapper

@speedTest
def bigLoop():
  for number in range(1, 20000):
    print(number)

bigLoop()



# assignment18
n=-1
def reverse_string(my_string):
   yield my_string[-1]
   yield my_string[-2]

# Reverse The String
for c in reverse_string("Elzero"):
  print(c)