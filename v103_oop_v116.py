
"""   OOP """

# ------------------------------------------
# v103: Object Oriented Programming => Intro --
# ------------------------------------------
# [1] Python Support Object Oriented Programming
# [2] OOP Is A Paradigm Or Coding Style
#     OOP Paradigm =>
#       Means Structuring Program So The Methods[Functions] and Attributes[Data]
#       Are Bundled Into Objects
# [3] Methods => Act As Function That Use The Information Of The Object
# [4] Python Is Multi-Paradigm Programming Language [Procedural, OOP, Functional]
#     - Procedural => Structure App Like Recipe, Sets Of Steps To Make The Task
#     - Functional => Built On the Concept of Mathematical Functions
# [5] OOP Allow You To Organize Your Code and Make It Readable and Reusable
# [6] Everything in Python is Object
# [7] If Man Is Object
#     - Attributes => Name, Age, Address, Phone Number, Info [Can Be Differnet]
#     - Methods[Behaviors] => Walking, Eating, Singing, Playing
# [8] If Car Is Object
#     - Attributes => Model, Colour, Price
#     - Methods[Behaviors] => Walking, Stopping
# [9] Class Is The Template For Creating Objects [Object Constructor | Blueprint]
#     - Class Car Can Create Many Cars Object

# v104: Object Oriented Programming => Class Syntax and Info --

# [01] Class is The Blueprint Or Construtor Of The Object
# [02] Class Instantiate Means Create Instance of A Class
# [03] Instance => Object Created From Class And Have Their Methods and Attributes
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
# [06] Class May Contains Methods and Attributes
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create Object From Class
# [09] __init__ Method Is Initialize The Data For The Object
# [10] Any Method With Two Underscore in The Start and End Called Dunder or Magic Method
# [11] self Refer To The Current Instance Created From The Class And Must Be First Param
# [12] self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object

# Syntax
# class Name:
#     Constructor => Do Instantiation [ Create Instance From A Class ]
#     Each Instance Is Separate Object
#     def __init__(self, other_data)
#         Body Of Function


class AliClass:
  def __init__(self):
    print("A New Member Has Been Added")

member_one = AliClass()
member_two = AliClass()
member_three = AliClass()

print(member_one.__class__)                   #__class__ :to know the class name

# v105 : Object Oriented Programming => Instance Attributes and Methods 
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself

class CreateName :
    def __init__(self,fname,sname,tname):
        
       self.firstname=fname                 #parameters 
       self.secondname=sname
       self.thirdname=tname
       
name1=CreateName("ali","mohamed","mahmoud")
name2=CreateName("Ahmed","mohamed","mahmoud")
name3=CreateName("ali","mohamed","ziad")
print(name1.firstname,CreateName("ali","mohamed","mahmoud").secondname,CreateName("ali","mohamed","mahmoud").thirdname) 
print(name2.secondname)          #access with instance or attribute
print(name2.thirdname)


# v106&107&108 :OOP (instance method)&class attribute
class CreatefullName :
    class_attribute=0                       ##Class Attributes: Attributes Defined Outside The Constructor
    
    @classmethod                            #class method access with cls and in other position we use class name to get the method
    def say_hello(cls):                     
        return f"hello {cls.class_attribute}"
    
    @staticmethod                            #static method access without any thing and in other position we use class name
    def say_by():
        return f"GoodBy"
    
    def __init__(self,fname,sname,tname,gender):    #constructor
       self.firstname=fname                 #instance attribute 
       self.secondname=sname
       self.thirdname=tname
       self.gender=gender
       CreatefullName.class_attribute +=1
       
    def controll_gender(self,funcname):                 #can add attributes to function
        if self.gender =='male' :
            return f"{funcname} =>{CreatefullName.say_hello()} mr {self.firstname}"
        elif self.gender =='female' :
            return f"{funcname} =>{CreatefullName.say_hello()} ms {self.firstname}"
        else :
            return f"{CreatefullName.say_hello()} {self.firstname}"

    def get_full_name(self):
        return f" {self.firstname} {self.secondname} {self.thirdname}"

    def all(self):
        add_attributes=self.controll_gender("Good")
        CreatefullName.class_attribute +=1
        return f"{add_attributes},{self.get_full_name()},{CreatefullName.class_attribute},{CreatefullName.say_by()}"  #can access any function 
    
    def delete(self):
          CreatefullName.class_attribute -=1
          return f"After Deleting{CreatefullName.class_attribute}" 
          
clas=CreatefullName("ali","mohamed","mahmoud","male")
print(clas.all())
print(clas.delete())
clas2=CreatefullName("nada","mohamed","mahmoud","female")
print(clas2.all())
print(clas2.say_hello())
print(clas2.say_by())

#  v109 :Object Oriented Programming => Magic Methods 
# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
#           Called When We Use the Built-in len() Function on the Object
class skills:
    def __init__(self) -> None:
        self.skills=['football','basket']
    def __str__(self) -> str:
        return f"my skills is {self.skills}"
    def __len__(self):
        return len(self.skills)
myskill=skills()
print(myskill)
print(myskill.__class__)
print(len(myskill))
print(dir(myskill))


class InheritClass(CreatefullName):
    def __init__(self, fname, sname, tname, gender,skill):
        super().__init__(fname, sname, tname, gender)
        
        self.skill=skill                                #can add any other instance
        print(f"{self.firstname} {self.secondname} {self.thirdname},my skill is {self.skill}")
    def get_skill(self):
        print(f"{self.skill}") 
myinherit=InheritClass("ali","mohamed","mahmoud",'male','football')
print(myinherit)
print(myinherit.all())
print(myinherit.get_skill())

# 110 : Object Oriented Programming => Multiple Inheritance --

class BaseOne:
  def __init__(self):
    print("Base One")

  def func_one(self):
    print("One")

class BaseTwo:
  def __init__(self):
    print("Base Two")

  def func_two(self):
    print("Two")

class Derived(BaseOne, BaseTwo):
  pass

my_var = Derived()
# print(Derived.mro())
# print(my_var.func_one)
# print(my_var.func_two)
my_var.func_one()
my_var.func_two()

class Base:
  pass
class DerivedOne(Base):
  pass
class DerivedTwo(DerivedOne):
  pass

# v111: Object Oriented Programming => Polymorphism 

class A:
  def do_something(self):
    print("From Class A")
    raise NotImplementedError("Derived Class Must Implement This Method")

class B(A):
  def do_something(self):
    print("From Class B")

class C(A):
  def do_something(self):
    print("From Class C")

my_instance = B()
my_instance.do_something()


# v113: Object Oriented Programming => Encapsulation 
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties

class Encapsulation:
    def __init__(self,name,birthday):
        self._name=name                  #protect
        self.__birthday=birthday         #private
        
my=Encapsulation("ali","7,4")      
print(my._name)
print(my._Encapsulation__birthday)

# v114:Getters & Setters
class GettetAndSetter:
    def __init__(self,name) -> None:
       self.__name=name
     
    # @property  
    def getter(self):
        return self.__name
    def setter(self,new_name):
        self.__name=new_name
        return self.__name

getandset=GettetAndSetter("ali")
print(getandset.getter())
print(getandset.getter())
print(getandset.setter("Ahmed"))

# v116: Object Oriented Programming => ABCs => Abstract Base Class --
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class

from abc import ABCMeta, abstractmethod

class Programming(metaclass=ABCMeta):        #base to walk on it
  @abstractmethod
  def has_oop(self):
    pass

  @abstractmethod
  def has_name(self):
    pass

class Python(Programming):
  def has_oop(self):
    return "Yes"

class Pascal(Programming):
  def has_oop(self):
    return "No"

  def has_name(self):
    return "Pascal"

one = Pascal()
print(one.has_oop())
print(one.has_name())








