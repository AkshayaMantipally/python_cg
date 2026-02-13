import copy
a=[1,2,3]
b=copy.copy(a)#only the inner objects are copied
a.append(4)
print(a)
print(b)


###SLICING
s="BVRIT COLLGE of engineering"
print(s[0:5:1])#-->1 by default value
#print(s[0:5]) #-->5 index is excluded
print(s[-28:-22])
print(len(s))
print(s[-11:])
print(s[-len(s):-(len(s)-5)])
print(s[:-12:-1])
st={1,2,3}

print(1,2,3,4,5,end='#')
print(1,2,3,4,sep='\t',end='#')
print(1,2,3,4,sep=' ',end='\n')
print(1,2,3,4,5,end='#')
x=print('hello')
print(x)


##COMPREHENSION
lst=[i for i in range(1,11)]  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)

lst1=[i for i in range(1,10) if i%2!=0]
print(lst1)
lst2=[i**2 if i%2==0 else i**3 for i in range(1,10)]
inp="python is very very easy language"
lst=[(word.lower(),len(word)) for word in inp.split()]
print(lst)


set={i:i**2 if i%2==0 else i**3 for i in range(1,10)}
print(set)

inp1="Hai HeLLO"
set1 = {ch: ord(ch)   for ch in inp1 if ch.isupper()}
print(set1)


#REGEX
import re



