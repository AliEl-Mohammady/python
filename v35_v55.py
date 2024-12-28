             #assignment operators,comparison operators,input,if,while loop,for loop

# # v35 :assignment operators(+=,/=,-=,*=,**=,//=,%=)
# a=10
# a//=2
# a**=2
# print(a)

# # v36 :comparison operators(=,>,<,<=,>=)
# print(a<10)
# print(a==10)
# print(a>10)
# print(a<=10)
# print(a>=10)

# # assignment7
# html = 80
# css = 60
# javascript = 70
# print(html>50 and css >50 and javascript> 50)

# num_one = 10
# num_two = 20

# result=num_one+num_two
# print(result)
# result=num_one+num_two
# print(((result**3)%26000)/5)

# #########################################################################################################################

# v38: input
# name =input('what\'s your name?')
# age=input('what\'s your age?')
# langauge=input('what\'s your langauge?')

# print(f"Hello {name.capitalize()} your age is {int(age):.2f} and your languge is {langauge.strip()}")

# v39: input practice
# name =input('what\'s your name?')
# email=input('what\'s your email?')

# print(f"Hello {name.capitalize().strip()} your email is {email} and username is {email[:email.index('@')]} and websilte is {email[email.index('@')+1 :]}")

# ###################################################################################################################

# # v41&v42: if and elif and else and nested if
# name='ali'
# if name[0]=='a' :
#     if name =='ali':
#         print('hello mr ali')
# elif name =='ahmed':
#     print('hello mr ahmed')
# else :
#     print('hello')
    
# # v43: ternary if and short if (condition if true | if condition |else |condition if false)
# a=2
# print('a=4'if a*2==8 else 'a=5')    

# # v44: if with in and not in 
# countries =['Eyg','Ksa']
# if 'Eyg' in countries : 
#     print('hello from egypt')
# if 'Ey' not in countries : 
#     print('hello from egypt')
    
    
# # assignment9
# num1 = int(input('you first number?').strip())
# num2 = int(input('you second number?').strip())
# operation = input("+ Or - Or * Or / Or %").strip()

# if operation== '+' :
#     result=num1+num2
#     print(result)
# elif operation== '-' :
#     result=num1-num2
#     print(result)
# elif operation== '*' :
#     result=num1*num2
#     print(result)
# elif operation== '/' :
#     result=num1/num2
#     print(result)
    
# age = 15
# print("App Is Suitable For You" if age >16 else "App Is Not Suitable For You")

# country = input("Input Your Country").strip().capitalize()
# countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
# price = 100
# discount = 30

# if country in countries :
#     print(f"Your Country Eligible For Discount And The Price After Discount Is ${price-discount}")
# else :
#     print(f"Your Country Not Eligible For Discount And The Price Is ${price}")
    
# ###############################################################################################################    

# v47: while condition_is_true : code run  the main difference is while take a condition but for not take just looping

# a=0
# while a <10 :
#     a += 1
#     print(a)
# while False :
#     print("will not print anything")

# # v47: while-loop 
# countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
# a=0
# while a < len(countries) :
#     print(f"{a+1}-{countries[a]}")
#     a += 1
# else :
#     print("after end of loop")

# # assignment10
# # Input
# num = int(input('enter number !'))

# while num>1 :
#     if num-1==6:
#         pass
#     else :
#         print(num-1)
#     num-=1

    
# # Input
# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
# a=0
# b=[]
# while a <len(friends) :
#     if friends[a]==friends[a].capitalize() :
#         print(friends[a])
#     else :
#         b.append(friends[a])
        
#     a +=1
# else :        #used after end of looping
#     print(f"Friends Printed And Ignored Names Count Is {len(b)}")

# # Code
# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
# while skills:
#     print(f"I have expertise in {skills.pop(0)}")
  
###################################################################################################################
# v51: for loop  the main difference is while take a condition but for not take condition just looping 
name='ali'
for a in name :
    print(a)
else :
    print("looped finished")
    
# v53: nested for loop    
dict_loop={'a' : {'a':'ali','b':'ahmed'}}
for rec in dict_loop :
    for line in dict_loop[rec] :
        print(dict_loop[rec][line])
        
# v54: continur and break and pass for loop
lists=range(2,9)
for num in lists:
    if num == 3 :
        continue
    if num == 21 :
        break
    if num == 4 :
        pass
    print(num)   
  
# v55: advanced for loop        
dict_loop={'a' : {'a':'ali','b':'ahmed'}}
for rec_valur,rec_vlue in dict_loop.items() :
    for line,value in rec_vlue.items() :
        print(value)
      

# assignment11
mylist=range(1,21)
for l in mylist :
    if l in [6,8,12] :
        continue
    print(str(l).zfill(2))
else :
    print("loop is done")

 # Input
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
a=100
b=80
c=40
d=20

for rec in students :
    total=0
    print(f"-- Student Name => {rec}")
    for line in students[rec] :
        if students[rec][line] =="A" :
            print(f"- {line} => {a} Points")
            total+=a
        if students[rec][line] =="B" :
            print(f"- {line} => {b} Points")
            total+=b
        if students[rec][line] =="C" :
            print(f"- {line} => {c} Points")
            total+=c
        if students[rec][line] =="D" :
            print(f"- {line} => {d} Points")
            total+=d
    print(f"Total Points For {rec}  Is {total}")
    
# Needed Output
"------------------------------"
"-- Student Name => Ahmed"
"------------------------------"
"- Math => 100 Points"
"- Science => 20 Points"
"- Draw => 80 Points"
"- Sports => 40 Points"
"- Thinking => 100 Points"
"Total Points For Ahmed Is 340"
"------------------------------"
"-- Student Name => Sayed"
"------------------------------"
"- Math => 80 Points"
"- Science => 80 Points"
"- Draw => 80 Points"
"- Sports => 20 Points"
"- Thinking => 100 Points"
"Total Points For Sayed Is 360"
"------------------------------"
"-- Student Name => Mahmoud"
"------------------------------"
"- Math => 20 Points"
"- Science => 100 Points"
"- Draw => 100 Points"
"- Sports => 80 Points"
"- Thinking => 80 Points"
"Total Points For Mahmoud Is 380"
    
    