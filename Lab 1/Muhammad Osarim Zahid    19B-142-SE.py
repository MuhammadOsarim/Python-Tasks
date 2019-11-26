#!/usr/bin/env python
# coding: utf-8

# In[5]:


original_list1 = [10,22,44,23,4]
new_list2 = list(original_list1)
print(original_list1)
print(new_list2)


# In[6]:


#Create an empty tuple
x=()
print(x)
#Create an empty tuple with tuple()function built-in python
tuple1 = tuple()
print(tuple1)


# In[8]:


#Create a tuple with different data types
tuple2 = ("tuple",False,3.2,1)
print(tuple2)


# In[9]:


#Get an item of the tuple
tuplex = ("U","I","T",2,0,1,8,"b","a","t","c","h")
print(tuplex)
#Get item(3th element from last)by index negative
item1 = tuplex[-4]
print(item1)


# In[48]:


#Question 1
from datetime import date
Date_1 = date(2019,11,3)
Date_2 = date(2019,11,6)
delta = Date_2 - Date_1
print (delta.days)


# In[15]:


#Question 2(a)
from math import sin
from math import pi 
length = eval(input("Enter Length"))
angle = eval(input("Enter angle"))
angle = pi * angle // 180
height = length * (sin(angle))
print("the height is" ,height)


# In[16]:


#Question 2(b)
from math import sin
from math import pi 
length = eval(input("Enter Length"))
angle = eval(input("Enter angle"))
angle = pi * angle // 180
height = length * (sin(angle))
print("the height is" ,height)


# In[17]:


#Question 2(c)
from math import sin
from math import pi 
length = eval(input("Enter Length"))
angle = eval(input("Enter angle"))
angle = pi * angle // 180
height = length * (sin(angle))
print("the height is" ,height)


# In[18]:


#Question 2(d)
from math import sin
from math import pi 
length = eval(input("Enter Length"))
angle = eval(input("Enter angle"))
angle = pi * angle // 180
height = length * (sin(angle))
print("the height is" ,height)


# In[44]:


#Question 4(a)
monthsL = ["Jan","Feb","Mar","May"]
monthsL.insert(3,"Apr")
print(monthsL)

monthsT =["Jan","Feb","Mar","May"]
monthsT.insert(3,"Apr")
print(monthsT)


# In[45]:


#Question 4(b)
monthsL = ["Jan","Feb","Mar","May"]
monthsL.append("Jun")
print(monthsL)

monthsT =["Jan","Feb","Mar","May"]
monthsT.insert(3,"Apr")
print(monthsT)


# In[46]:


#Question 4(c)
monthsL = ["Jan","Feb","Mar","May"]
monthsL.pop()
print(monthsL)

monthsT =["Jan","Feb","Mar","May"]
monthsT.pop()
print(monthsT)


# In[47]:


#Question 4(d)
monthsL = ["Jan","Feb","Mar","May"]
monthsL.pop(1)
print(monthsL)

monthsT =["Jan","Feb","Mar","May"]
monthsT.pop(1)
print(monthsT)


# In[50]:


#Question 6
a=6
b=7
c=a+b/2
inventory=["paper","staples","pencils"]
first="john"
middle="fizzegaed"
last="kennely"
fullname=first + middle + last
print(fullname)

