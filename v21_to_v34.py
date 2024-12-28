               ##types [list,tuple,set,dictionary]
               
# # v21 :lists
# mylist=['ali',10,45,True,[1,2,8]]

# print(mylist[0])
# print(mylist[0:3])
# print(mylist[-1])
# print(mylist[::2])
# mylist[0]="Ahmed"
# print(mylist)
# mylist[0:2]=["Ahmed"]
# print(mylist)
# mylist[0:2]=[]
# print(mylist)

# # v22 :lists method p1
# mylist=['ali',10,45,True,[1,2,8]]
# mylist.append(10)
# print(mylist)
# mylist.append([10,20])              #append :add content to list as it given
# print(mylist)
# mylist.extend([10,20])              #extend :add content to list but as single item
# print(mylist)
# mylist.remove([10,20])              #remove :remove content as it given but only first one 
# mylist2=[1,5,9,555]
# mylist2.sort()                      #sort :sort or arrange items from small to large
# print(mylist2) 
# mylist2.sort(reverse=True)          #sort(reverse=True)  :sort or arrange items from large to small 
# print(mylist2)
# mylist2.reverse()                   #reverse()  :reverse items only not arrange or sort 
# print(mylist2)

# # v23 :lists method p2
# list_method=['ali',5,True]
# mylist2.clear()                     #clear()  :remove all items of list
# print(mylist2)
# copylist=list_method.copy()         #copy()  :copy items of the list but not including any edit in primary list  
# print(copylist)
# print(list_method.count(5))         #count(item)  :count  of this repeated item
# list_method.insert(25,-1)           #insert(index,item)  :add items to list but in specific position
# print(list_method)
# print(list_method.pop(-1) )         #pop(index)  :get item from list 

# # assignment4
# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# print(friends[0])
# print(friends.pop(0))
# friends[-2:]=["ali","ali"]
# print(friends)
# friends.insert(0,"ahmed")
# print(friends)
# friends.append("ahmed")
# print(friends)

# friends = ["Ahmed", "Sayed"]
# employees = ["Samah", "Eman"]
# school = ["Ramy", "Shady"]
# friends.extend(employees)
# friends.extend(school)
# print(friends)
# print(len(friends))

# ###############################################################################################################
# # v24 :tuple 
# friends = ("Osama", "Ahmed", "Sayed", "Ahmed")
# print(friends*3)                     #string repeat using (*)
# print(friends[2])
# # friends[2]="ali"                 #can't edit or remove or do any thing it is immutable 

# # v25 :tuple method
# print(friends.count("Osama"))
# print(friends.index("Osama"))
# a,b,_,d=friends                    #using _ to unassign variable
# print(a)

# # assignment5
# f='elzero',friends[1],friends[2]
# print(f)

# nums = (1, 2, 3)
# letters = ("A", "B", "C")
# f=nums+letters                     #can add tuples like string 
# print(f)


###################################################################################################################################
# # v26 :set{}

# # myset={'ali',1,5.5,(1,2,8),'ali'}               #unique :cant repeat item  unhashable type
# # myset={'ali',1,5.5,(1,2,8),'ali'}               #not order                 unhashable type
# # # myset[0]                                      #not indexed
# # myset={'ali',1,5.5,(1,2,8),{'a:1'},['ali',2]}   #can't add list or dictinary 
# myset={'ali',1,5.5,(1,2,8)}                       #only string ,numbers and tuble
# print(myset)

# # v27 :set{}methods
# print(myset.clear())                              #clear() :to remove
# myset={'ali',1,5.5,(1,2,8)}                      
# myset.add("ahmed")                                #add() :to add items to set
# print(myset)  
# myset2={'ali',20}
# a=myset2.union(myset)  #= myset2 | myset          #union() :to add set to other set but must store in variable                              
# print(myset2|myset)
# b=a.union(['myset','ai'])
# print(b)                        
# print(myset2)                                     #the original set stay as it was
# myset2.update(myset)                              #update() :to add set to other set(modify on set)
# print(myset2)    
# c=myset2.copy()                                   #copy()  :copy items of the set but not including any edit in primary list  
# print(c)                          
# myset2.remove("ali")                              #remove()  :remove one item of the set but if not found get error
# print(myset2) 
# myset2.discard("ayad")                            #discard()  :remove one item of the set but if not found pass it not get error
# print(myset2) 
# print(myset2.pop())                               #pop()  :get random number
 

# # v28 :set{}methods p2
# a={4,'ali',88}
# b={20,'ali',88.5}
# print(a-b) 
# print(a.difference(b))                           #a.difference(b)= a-b :items found in a and not found in b and not update on original set
# print(a)
# a.difference_update(b)                           #a.difference_update(b):items found in a and not found in b and update on original set
# print(a)
# a={4,'ali',88}
# b={20,'ali',88.5}
# print(a&b) 
# print(a.intersection(b))                           #a.intersection(b)= a&b :items found in a and found in b and not update on original set
# print(a)
# a.intersection_update(b)                           #a.intersection_update(b):items found in a and found in b and update on original set
# print(a)
# a={4,'ali',88}
# b={20,'ali',88.5}
# print(a^b) 
# print(a.symmetric_difference(b))                   #a.symmetric_difference(b)= a^b :items found in a and not found in b and items found in b and not found in a and not update on original set
# print(a)
# a.symmetric_difference_update(b)                   #a.symmetric_difference_update(b):items found in a and not found in b and items found in b and not found in a and update on original set
# print(a)

# # v29 :set{}methods p3
# a={1,5,8,9}
# b={1,5}
# print(a.issuperset(b))                             #issuperset() :if all items of b in a  return true or false
# print(a.issubset(b))                               #issubset() :if all items of a in b  return true or false
# print(a.isdisjoint(b))                             #isdisjoint() :if all items of a and b deference from each other return true or false

######################################################################################################################################

# v30 :dictionary{}
b={1,5}
info={
    'name':'ali',
     1:1,
    ('country','city'):'bani-suef',
    'fav':(1,2,8),
    'lang':['html','js'],
    'sports':{
        'football':1,
        'basket':2},
    'numbers':b,
}
print(info)                             #dict is unique cant repeat keys and not indexing
print(info.keys())                      #keys() :to print dict keys and keys can be only (str,num,tuple) 
print(info.values())                    #values() :to print dict values and values can be any type (str,num,tuple,dict,list ,set or variable) 
print(info['sports'])                   #can access using [] or .get()
print(info.get('sports')) 

# v31 :dictionary{} method
# print(info.clear())                     #clear() : remove all items
c=info.copy()
print(c)                                #copy()  :copy items of the dict but not including any edit in primary dict  
info.update({"sleep":"8hr"})            #update({"key":"value"})  :add items to dict and can use ["key"]=["value"]
info["wake"]="9hr"
print(info)
print("="*40)

# v32 :dictionary{} method p2
info.setdefault("age",39)
print(info)
print(info.setdefault("age",40))        #setdefault(key,value)  :if find key will print it's value it or will ceate new dict
print(info.setdefault("ag",40))
print(info)
print(info.popitem())                   #popitem() :print last item added to dict
print(info.items())                     #items() :retuen dict to list of tuples every tuple consist of (key,value) 
b=["x","y"]
c=10
print(dict.fromkeys(b, c))              #dict.fromkeys(iterable items, values) :create dictionary

# assignment6
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list=list(set(my_list))
print(unique_list)
print(unique_list[0:4])

nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums.union(letters))
print(nums.symmetric_difference(letters))
nums.update(letters)
print(nums)

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_two.issuperset(set_one))
print(set_one.issubset(set_two))

#####################################################################################################################
# # v33 :boolean :True or False
# print(100==100)
# print(bool(""))
# print(bool([]))
# print(bool())
# print(bool(''))
# print(bool({}))
# print(bool(False))
# print(bool(None))

# # v34 :boolean operators
# a='ali'
# age=45
# country='Eygpt'
# print(a =='ali' and age >10 and country=='Eygpt')    #and
# print(a =='ali' or age >10 and country=='Ksa')       #or
# print(a =='ali' and not age >10 and country=='Ksa')  #not



