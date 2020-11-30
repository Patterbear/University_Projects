#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Scope issues
def f(x):
    def g():
        x = 10
        return x
    x = x+2
    g()
    return x
x = 5
y = f(x)
print(y)


# In[15]:


t0 = () # empty tuple
t = (1, 'a', 2)
#t[0]  # will return 1
#t[0:1] # will return (1,)
# the extra comma is because the tuple has one element
#t[0:2] # will return (1, 'a')
#len(t) # will return 3
#t+t # will return (1, 'a', 2, 1, 'a', 2)
#t+('b',) # will return (1, 'a', 2, 'b')
#t[1] = 3 # will give an error as t is immutable'''
print(t0)
print(t)


# In[19]:


t[0]


# In[4]:


t[0:1]


# In[5]:


t[0:2]


# In[6]:


len(t)


# In[7]:


t+t


# In[8]:


t+('b', )


# In[20]:


t[1]=3


# In[18]:


x= 2; y = 5
x = y
y = x
print(x, y)


# In[4]:


x = 2; y = 5
(x, y) = (y, x) #same as x, y = y, x
print(x, y)


# In[5]:


x=2; y = 5
tmp = x
x = y
y = tmp
print(x, y)


# In[6]:


def quotient_and_rem(a, b):
    q = a//b #integer division
    r = a%b
    return (q, r)
(q, r) = quotient_and_rem(132, 11)
a = quotient_and_rem(132,11)
print(a)


# In[7]:


def get_stats(data):
    ''' input data is made of ((int, string), (int, string), ...)'''
    nums = ()
    words = ()
    for t in data:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    minNum= min(nums)
    maxNum= max(nums)
    numOfUniqueWords= len(words)
    return (minNum, maxNum, numOfUniqueWords)


# In[8]:


(1, 2, 4) > (1, 3, 10)


# In[9]:


txt = 'I love Python more than Java'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)
print(t)


# In[10]:


a = 'apple'
b = 'apple'
a is b


# In[11]:


l1 = [1, 2, 3]
l2 = [1, 2, 3]
l = l1
print(l1 is l2)
print(l is l1)


# In[12]:


l = [0, 2, 4]
#l_copy = l[:]
l_copy = l.copy()
l_copy.append(6)
print(l)
print(l_copy)


# In[13]:


l1 = [-3, 4, -10, 2]
l2 = [0, -2, 3, -10]
l1_s = l1.sort()
l2_s = sorted(l2)
print(l1)
print(l1_s)
print(l2)
print(l2_s)


# In[14]:


def comp_diff(l1, l2):
    for e in l1:
        if e in l2:
            l1.remove(e)
    return l1
l1 = [0, 2, 4, 6]
l2 = [0, 2, 8, 10]
comp_diff(l1, l2)


# In[15]:


def comp_diff_corrected(l1, l2):
    l1_copy = l1[:]
    for e in l1_copy:
        if e in l2:
            l1.remove(e)
    return l1
a = [0, 2, 4, 6]
b = [0, 2, 8, 10]
comp_diff_corrected(a, b)


# In[16]:


l = [[1, 2], ['a', 'b', 'c'], [0, 2, 4]]
d = [[1, 3], [-2, 4]]
ds = sorted(d)
print(ds)
l[1][2] # returns c
l.append([(1, 'a'),(26,'x')])
len(l) #returns 4
len(l[3]) #returns 2
l[3][0] #returns (1, 'a')
#sorted(l)


# In[17]:


[-2, 4]<[1, 2]


# In[21]:


import numpy as np
a = np.array([1, 2, 3, 4])


# In[22]:


a


# In[24]:


b = np.array(range(1, 10))
print(b)


# In[25]:


l = [x+1 for x in range(1, 10)]
print(l)


# In[26]:


c = np.array(l)
print(c)


# In[27]:


c[2]


# In[28]:


d = c.reshape(3, 3)
print(d)


# In[29]:


d[2][2]


# In[19]:


x = np.array([1, 2, 3])
print(x)


# In[20]:


b = np.array(range(1, 5))
l = [x**2 for x in range(1, 5)]
c = np.array(l)
x = b+3 #add 3 to each element of b
y = b*2 #multiply each element by 2
s = b+c #add the vectors
p = b*c #mutiply the two vectors element wise
ratios = b/c #divides the two vectors element-wise
print(ratios)


# In[21]:


l = range(1, 10)
#ls = l**2 # leads to TypeError
a = np.array(l) 
asquared = a**2 # gives the squares OK
ls = asquared.tolist() #convert array to list
lsquared = [e**2 for e in l] #a bit verbose!
# Or worse
lsquared = []
for e in l:
    lsquared.append(e**2)
print(lsquared)


# In[23]:


from functools import reduce
def squared(x):
    return x*x
def sum(x,y):
    return x+y
l = [1, 2, 3, 4, 5]
lsquared = list(map(squared, l))
sum_of_squared = reduce(sum, lsquared)
print(lsquared)
print(sum_of_squared)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




