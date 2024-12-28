                     ## introduction,variable,string and numbers ##

print("ali")
print(type("ali")) # str => string
print(type(1)) # int => integer
print(type(1.5)) # float
print(type(2==2)) # bool => boolean
print(type([1,2,5,8])) # list
print(type((1,2,5))) # tuple 
print(type({"one":1})) # dict => dictionry

# v7,v8 :variables
name ="ALI"
_name ="mohamed"
name_10 ="mahmoud"
print(name)
print(_name)
print(name_10)

help("keywords")  #reserved words
a,b,c = 1,2,3

# v9 : escape sequence character
print("ali \n mohamed")                 # \n :to break line and start new line
print("ali \' mohamed\' \\ mahmoud")    # \ :to add special caracters
print("ali\
    mohamed\
    kkk")                               # \ :to collect lines(ignore new line)
print("ali\bbmohamed")                   # \b :to back space or remove one character before it
print("ali13589\rmohamed")              # \r :to replace
print("ali\tmohamed")                   # \t :to add indent

# v10 :concatination
a="hello"
b="friend"
print(a+b)
print(a+" "+b)
print(a+"\n"+b)

#assign1################################################################################################################

# v11 :string
a="""ali
mohamed
mahmoud"""
b="ali \nmohamed \nmahmoud"
print(a)
print(b)

# v12 :indexting and slicing
new='     love 2f sports      '
print(new[3]) #indexting[num] 
print(new[3:6]) #slicing[num:num] 
print(new[3:6:2]) #slicing[num:num:step] 

# v13 :strip,title,capitalize,upper,lower and zfill
print(new.strip())                # strip,lstrip,rstrip :to remove spacing
print(new.lstrip().title())       #translate to upper of the first letter with letter after num
print(new.rstrip().capitalize())  #translate to upper of the first letter without letter after num
print(new.strip().upper())        #translate to uppercase
print(new.strip().lower())        #translate to lowercase
a,b,c='1',2,50
print(a.zfill(3))                 #translate to lowercase

# v14 :strip,title,capitalize,upper,lower and zfill
a="let's-Play-football"
print(a.split("-"))               #return list of words at split (where to space,num of space)
print(a.rsplit("-",1))            #return list of words at split from right (where to space,num of space)
print(a.center(21,"#"))           #add decoration after and before string
print(a.count('l'))               #count num of repeat this search word                                  
print(a.count('l',0,6))
print(a.swapcase())               #change capital to small and reverse
print(a.startswith("l"))          #get true or false of start of 
print(a.endswith("l",0,10))       #get true or false of end of

# v15 :index,find,splitline,expandtab,rjust and ljust
a="hello from outside"
print(a.index('f'))               #return index of search letter and error if not found
# print(a.index('f',0,3))
print(a.find('f'))                #return index of search letter and -1 if not found
print(a.find('f',0,3)) 
print(a.ljust(20,"#"))            #justify string from left and complete string from right
print(a.rjust(20,"#"))            #justify string from right and complete string from left
a="""one
two
three"""
print(a.splitlines())             #return list of lines
print(a.expandtabs(20))           #control space of tabing
print(a.istitle())                #any function start with is return true or false

# v16:replace and join
alist=['a','b','c']
print(a.replace("o", "1",3))        #replace 
print(' '.join(alist))            #join list or any itterable type

# v17:FORmating old way => using placeholder %s :for string and %d for integers and %f for float number and % (variables)
n='ali'
a=10
rank=48.9
print('hollo %s ,is your age %d ? and your rank is %f ?' % (n,a,rank))
print('hollo %.2s ,is your age %d ? and your rank is %.2f ?' % (n,a,rank))  #can use numbers before d or s to controll digits and letters truncate

# v18:FORmating new way => using placeholder {index:.2s/._d/.2f} and .format(variables)
n='ali'
a=10125785
rank=48.9
print('hollo {} ,is your age {} ? and your rank is {} ?' .format(n,a,rank))
print('hollo {:s} ,is your age {:d} ? and your rank is {:f} ?' .format(n,a,rank))       #can use :s or :d or :f
print('hollo {0:s} ,is your age {2:f} ? and your rank is {1:d} ?' .format(n,a,rank))    #can use (1:) for index
print('hollo {0:.2s} ,is your age {2:.2f} ? and your rank is {1:d} ?' .format(n,a,rank))#can use (:.2) to truncate
print('hollo {0:s} ,is your age {2:f} ? and your rank is {1:,d} ?' .format(n,a,rank))   #can use (:,d) to format big numbers like format mony

    #FORmating new way in version 3.6 +
print(f'hollo {n} ,is your age {a} ? and your rank is {rank} ?')  
    

# assignment2
name = "#@#@Elzero#@#@"
print(name.strip('#@#@'))

msg = "I Love Python And Although Love Elzero Web School"
print(msg.count('Love'))

name = "Elzero"
print(name.index("z"))

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace('<3', 'Love',1))

name = "Osama"
age = 38
country = "Egypt"
print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")

################################################################################################################

# v19:Numbers
a=18                                                           #int num
b=48.2                                                         #float num
c=44+9j                                                        #complex num
print(type(a),type(b),type(c))
print(float(a))                                                #convert integer to float
print(format(a, '.10f'))                                       #convert integer to float and controll digits
print(complex(a))                                              #convert integer to complex
print(int(b))                                                  #convert float to integer
print(complex(b))                                              #convert float to complex
print(f"real part is {c.real} and imaginary part is {c.imag}") #get real and imaginary numbers

# v20:Arethimetic
print(1+2)              #addition
print(1- -22)           #substraction
print(1*22)             #multibulation
print(1/-22)            #division
print(2**22)            #exponent
print(23%2)             #modulus
print(23//2)            #floor divesion

# assignment3
num = 10
print(float(num))
print(format(num, '.10f'))


