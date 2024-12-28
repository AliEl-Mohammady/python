                #Function and file handling#

#v56:function
def first_function():
    print("firstt function")
    return "firstt function"
first_function()
    
# v57 :parameters and arguments
def addition(n1,n2):  #n1,n2 :parameters
    print(n1+n2)
addition(2,10)        #n1,n2 :arguments
    
# v61,61 :packing and unpacking arguments
skill=["css","html"]
myskill=["js","html"]
def details(name,*skills,**myskills):  #*Args :any number of args use ** to add dicts
    for skill in skills :
        print(f"hello {name},skill is {skill} ANd {myskill}")
details("ali",*skill)     
 
# v62 : global and local variable 
x=2
def one():
    global x
    x=10
    print(f"{x}")
def tow():
    print(f"{x}")    
print(x)
tow()    
one()   
print(x)
tow()  

# v63 :lambda function
hello=lambda name : f"Hello {name}"    
print(hello("Ali"))
   
# assignment15

# Tests
def addition(*n):
    num=0
    for line in n :
        if line ==10 :
            continue
        elif line ==5 :
            num -=line 
        else :
           num +=line 
    return num
print(addition(10, 20, 30, 10, 15)) # 65
print(addition(10, 20, 30, 10, 15, 5, 100)) # 160    
    
    
# Input
def show_skills(name,*language):
    if language :
        print(f"Hello {name} Your Skills Is")
        for line in language :
            print(f"-{line}")
    else :
        print(f"Hello {name} You Have No Skills To Show")
show_skills("Osama")


# Tests
arg={'h':10}
def get_score(**args):
    for rec_key,rec_valu in args.items():
        print(f"{rec_key}=>{rec_valu}")
get_score(**arg,python=80,math=50)

# Test 1
scores_list={
     "math":50,
     "science":20}
 
def get_the_scores(*name, **scores_list):
    if scores_list :
        if name :
            for n in name :
                print(f"Hello {n} This Is Your Score Table:")
        for key,value in scores_list.items() :
            print(f"{key}=>{value}")
    else :
        if name :
            for n in name :
                print(f"Hello {n} You Have No Scores To Show")
        
print("="*40)
get_the_scores("Osama")
get_the_scores(**scores_list)

##########################################################################################################################
# v65:file handling
import os
print(os.getcwd())                        #to get path of current directory of the current file
print(len(os.listdir()))
print(os.path.abspath("write.txt"))          #to get path of current file
print(os.path.dirname(os.path.abspath(__file__)))        #os.path.dirname():to get path of current directory and take argument :(file name)
print(os.chdir(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))))        #os.chdir():to change path of  directory to current directory and take argument :(file name)

file=open(r"/home/ali/courses/python/write.txt","r")

# v66:file reading to read files

# print(file)
# print(file.name)
# print(file.encoding)
# print(file.mode)
# print(file.read())
# print(file.read(1))
print(file.readline(2))
print(file.readlines())             #type :list

# v67:file writing and append 
write_file=open(r"/home/ali/courses/python/write.txt","w") #create file if not existing

write_file.write("/Hello from inside\n")                   #using write redit file with new line text
write_file.write("/Ali from inside\n")
mylist=["ali\n","asd"]
write_file.writelines(mylist)                              #using writelines must use list


append_file=open(r"/home/ali/courses/python/write.txt","a") #create file if not existing
append_file.write("/Hello from append_file\n")              #using append can't edit file just adding

# v67:file method
print(append_file.truncate(2))
print(append_file.tell())                                   #numbers of letters inside file
seek_file=open(r"/home/ali/courses/python/write.txt","r") 
append_file.seek(10)                                        #to move cursor to aposition
append_file.write("Aliiiiiiiiiiii")

# os.remove("/home/ali/courses/python/ali.txt")             #to remove a file using os library

# assignment16
assign_file=open(r"/home/ali/courses/python/write.txt","r") #create file if not existing
for line in assign_file:
    print(len(list(line)))
    