import keyword
print (keyword.kwlist)
print(len(keyword.kwlist))
help("keywords")
#False,None,True are special keywords as these start with the captial letter,these keywords can be assigned to the variables
a=5
#a=True
b=False
print(id(a))
print(id(5))
#Muliple variable creation:for creation no.on values should be equal to no.of variables
a,b,c,d=1,2,3,4
print(a,b,c,d)
#acc to industrial standard rule we need to create the variable of lrngth 72
#all the variables are identifiers but all the identifiers are not variables
print(type(a))
#there is default value and non default value.
#the non default value would br other than default value
#default:
print(int())#-->0
print(float())#-->0.0
print(bool())#-->False
#j,J is used for imaginary numbers
a=-5+6j
print(a)
print(complex()) #-->0j...j is imaginary where j=underroot-1

#Multivalued 
#string can be declaerd using single ,double,triple quotes    '',"",'""'
a="aks"
print(type(a))
print(a[2],a[-2])
#memory management 
#stack -->Varible stack   heap-->value space


#Modification:str we cannot reassign or change ..str is immutable(immutable is also called as hasable data type)
#if we can reassing or change then we say it as  mutable(mutable is also called as unhasable datatyoe)
##method in str
#upper-->str.upper();
print("aks".upper())
#lower-->str.lower()
print("AKSH".lower())
#captilize-->only the first character will become upper case remaining will be lower case
print("aKS".capitalize())
#title-->captalize each and every character of every word to capital and remaing lower
print("aks hay".title())
#isupper,islower
print("aks".isupper())
print("aks".islower())
print('123'.isdigit())#-->if all are number then return true else false
print('123'.isalpha())#-->if all are character then return true else false
print('aks'.count("a"))#-->it says how many time the letter is repeated i the str
#a.replace(old,new)-->it replaces the old word with the new word..this works only in print stmt...when we replace it does not change the actual str
print(a.replace("aks","sss"))
b=" hi world-aks "
print(b.split())#-->it split the str when there is space
print(b.split('-'))#-->it split the str when there is space
b.lstrip()#removes spaces from left
b.rstrip()#remove spcae from right
b.strip()#-->remove spaces from both the ends


ls=[1,2,3]
#List is mutable
ls.append(4)#we can only one number or arg at a time ..we cant append mutliple at a time so we use extend
l=[2,3]
ls.extend(l)
#insert:it insert value at which location we want
ls.insert(1,23)
print(ls)
#remove
ls.remove(1)#remove the first occurence if the arg is present
print(ls)
ls.pop(3) #at 3rd index it is removed
ls.pop()# it removes at last
print(ls)

#CLEAR -->ls.clear()-->removes all the elemets in the list

print(ls.index(2))#-->at which index 2 is present
ls.sort()#sort acc to asc
print(ls)
ls.sort(reverse=True)#sort acc to desc
print(ls)
ls.reverse()
print(ls)


#*TUPLE*
t=(10,20.5,'py')
#it is immutable data type..the data that should not be changed are stored on tuple 
print(dir(list))
#1️⃣ Dunder / Magic methods:__add__, __class__, __class_getitem__, __contains__, __delattr__, __delitem__, __dir__, __doc__, __eq__, __format__, __ge__, __getattribute__, __getitem__, __getstate__, __gt__, __hash__, __iadd__, __imul__, __init__, __init_subclass__, __iter__, __le__, __len__, __lt__, __mul__, __ne__, __new__, __reduce__, __reduce_ex__, __repr__, __reversed__, __rmul__, __setattr__, __setitem__, __sizeof__, __str__, __subclasshook__
#2️⃣ List-specific methods:append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
#3️⃣ Modifying (mutable) list methods:append, clear, extend, insert, pop, remove, reverse, sort
#4️⃣ Non-modifying list methods:copy, count, index

#Dictionary:key value pair
dict={"a":1,"b":2,"c":5,(1,2,3):4}
#dict={"a":1,"b":2,"a":4}-->a is updating with 4
#dict={"a":1,"b":2,[1,2,3]:3}-->it throws error because the key should be immutable,unique
print(dict)
print(dict["c"])#-->print the value present at the c key only if c is present in dict else if the key not prestn it will thriw the error
print(dict.get("k"))#-->print value of c in the dictionary .when the val not present it will print none
print(dict.get("k","not presetn"))#-->print value of c in the dictionary .when the val not present it will print what we have give
print(dict.keys())
print(dict.values())
print(dict.items())#-->convert key value to tuple -->dict_items([('a', 1), ('b', 2), ('c', 5), ((1, 2, 3), 4)])
dict.pop("c")
#dict.pop()#-->doesnot work for duct
print(dict)
set1=set()
print(type(set1))
s1={1,2,3.4,"f",1}#-->when ther are same values it will print only the single value
s1.add("s")
s2=s1.copy()#shallow copy:the changes in s1 further will not efect in s2
print(s1)
s2.pop()#-->based on index value specified
s2.remove(2)#-->if there is value 2 then it is removedelse if value not present it will throw an error
s2.discard(2)#-->if there is value 2 then it is removedelse if value not present it will not throw any error

print(s2)


###Binary-->bin(val)
###Octal-->Oct(val)
#m<<1 left shift
#m>>1 right shift
#m&n-->and->
#m|n-->or
#~m-->not 
#m^n-->xor

#identity operator
r=[1,2,3]
s=r
t=[1,2,3]
print(r is s)#same obj->true
print(r is t)##diff obj->false
print(r is not t)## different object -> True

#input
a=input("enter")#-->takes str as input
b=eval(input("msg:"))#-->we need to specify what we are giving like "hi" or [1,2] anything like int,float
#in while loop we doent use set or dict
#for loop we can use any collection
for i in range(1,6):
    print(i)
for ch in "pyton":
    print(ch)
print(list(range(5)))
print(list(range(1,5)))
print(list(range(1,5,3)))