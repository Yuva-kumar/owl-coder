#!/usr/bin/env python
# coding: utf-8

# In[8]:


#convert a number into binary
n=int(input())
s=''
for i in range(31):
    a=1
    b=1<<i
    if n&b>0:
        s+='1'
    else:
        s+='0'
print(s[::-1])        


# In[2]:


print(len('9'))


# In[11]:


# to find the number of bits which are required to binary representation
import math
n=int(input())
len=int(math.floor(math.log(n)/math.log(2)))+1
print(len)


# In[18]:


import math
n=int(input())
len=math.ceil(math.log2(n))
print(len)


# In[30]:


arr=[1,10,1,1]
s=''
for i in range(0,32):
    c=0
    for j in arr:
        a=1<<i
        if j&a>0:
            c+=1
    if c%3==0:
        s+='0'
    else:
        s+='1'
k=0
for i in range(len(s)):
    k+=int(s[i])*(2**i)
print(k)


# In[76]:


arr=[1,-10,1,2,2,1,2]
s=0
for i in range(0,32):
    c=0
    for j in arr:
        a=1<<i
        if j&a>0:
            c+=1
    if c%3==1:
        s=s|(1<<i)
print(s)


# In[64]:


arr=[1,-110,-111,-111,-111,2,2,1,2]
s=0
for i in range(0,32):
    c=0
    for j in arr:
        a=1<<i
        if j&a>0:
            c+=1
    if c%3==1:
        s=s|(1<<i)
if s in arr:
    print(s)
else:
    print(s-4294967296)


# In[ ]:





# In[71]:


arr=[-1,-100,-1,2,2,-1,2]
arr2=[i for i in arr if i<0]
arr1=[abs(i) for i in arr]
s=0
for i in range(0,32):
    c=0
    for j in arr1:
        a=1<<i
        if j&a>0:
            c+=1
    if c%3==1:
        s=s|(1<<i)
if len(arr2)%3==0:
    print(s)
else:
    print(-s)


# In[ ]:





# In[ ]:





# In[ ]:





# In[28]:


print(bin(4294967286)[2:])


# In[ ]:





# In[ ]:





# In[4]:


# to convert binary into decimal
a='10110'
b=a[::-1]
c=0
for i in range(len(a)):
    c+=int(b[i])*(2**i)
print(c)


# In[25]:


n=int(input())
s=''
for i in range(31):
    a=1
    b=1<<i
    if n&b>0:
        s+='1'
    else:
        s+='0'
s1=s[::-1]
for j in range(31):
    a=1<<j
    if int(s[j]) & a >0:
        print(j)    


# In[ ]:


n=int(input())
c=0
for i in range(31):
    for j in range(1,n+1):
        a=1<<i
        if j&a>0:
            c+=1
        


# In[ ]:


a,b=map(int,input().split())
l=[i for i in range(a+1,b)]


# In[ ]:


l=[3, 2, 1, 34, 34, 1, 2, 34, 2, 1]


# In[5]:


arr=list(map(int,input().split()))
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=arr[a]
    for i in range(a+1,b+1):
        c&=arr[i]
    print(c)


# # And

# In[23]:


import math
arr=list(map(int,input().split()))
for _ in range(int(input())):
    a,b=map(int,input().split())
    r=b-a+1
    k=max(arr)
    s=(int(math.log2(k)))+1
    ll=[]
    l2=[]
    for i in range(s):
        c=0
        for j in arr:
            x=1<<i
            if j&x>0:
                c+=1
            if a!=0:
                if j==arr[a-1]:
                    l2.append(c)
            if j==arr[b]:
                break
        ll.append(c)

    if a!=0:
        l1=[]
        for i in range(len(ll)):
            l1.append(ll[i]-l2[i])
    else:
        l1=ll
    k=0
    for i in range(len(l1)):
        if l1[i]==r:
            k+=2**i
    if k!=0:
        print(k)
    else:
        print(0)


# # or

# In[ ]:





# In[ ]:





# In[56]:


def fib(n):
    l=[0,1]
    for i in range(n+2):
        k=l[-1]+l[-2]
        l.append(k)
    return l
N=int(input())
a=fib(N)
a1=a[3:]
print(a1[N-1]**2)


# In[39]:


print(34**2)


# In[ ]:




