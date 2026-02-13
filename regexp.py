import re
s="python is very easy"
print(re.search("easy",s))#-->give where the word is in the sentence
print(re.match("easy",s))#-->it shows only if it in the beginning...if it is not presnt at the begininnig it wiil show none
  
#-->GROUP
print(r'\t')#--->r is used to convert the spacial behaviour to word
m=re.search(r"\d+","Age is 21")
print(m.group())


#-->GROUPS
m=re.search(r"(\d+)-(\d)","2025-245_123 28-67")
print(m.groups())

print(re.search(r"\d{2,4}","ID:1234"))  #{n,m}
print(re.search(r"ab*","a"))  #*(0 or more)
print(re.search(r"ab+","abb")) #(1 or more)
print(re.search(r"colou?r","color"))#?(0 or 1)
print(re.search(r"\d{4}","year 2025"))







##############Function##################
# def add(a,b):
#     return a+b
# a=int(input("enter"))
# b=int(input("enter"))
# print(add(a,b))

#1.waptp the palindrome number withou using slicing with help of function with arg and return type
#2.waptp the n number of prime number with the help of function with arg and return type and n should be the input from the user


def ispalin(n):
    x=n
    ans=0
    while(x>0):
        r=x%10
        ans=ans*10+r
        x=x//10
    return ans
n=909
x=ispalin(n)
print(x)
if n==x:
    print("is plaindrome")
else :
    print("not")










def isprime(n):
    prime = []
    num = 2

    while len(prime) < n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime.append(num)
        num += 1

    return prime


n = 7
result = isprime(n)
print(result)


#WAP to check whether the given data is float or not

flo=lambda x:"float" if type(x)==float else "no"
print(flo(10.5))

#WAP to print sum  of 3 nums
sum=lambda x,y,z:x+y+z
print(sum(1,2,3))