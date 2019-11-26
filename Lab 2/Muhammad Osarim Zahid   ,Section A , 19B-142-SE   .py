
# coding: utf-8

# In[5]:



# Math Operator in Python
# taking two values
a = 10
b = 22

#Using sum operator
print("Sum is:",a+b)
#Using subtract operator
print("Difference is:",a-b)
#Using multiplication operator
print("Division is:",a/b)
#Using integer division operator
print("Integer Division is:",a//b)
#Using power operator
print("Raised to the Power is:",a**b)
#Using modulo operator
print("Remaider is:",a%b)


# In[7]:


x=5
x +=3
print(x)

x=5
x -=3
print(x)

x=5
x *=3
print(x)

x=5
x /=3
print(x)

x=5
x %=3
print(x)

x=5
x //=3
print(x)

x=5
x **=3
print(x)

x=5
x &=3
print(x)

x=5
x|=3
print(x)

x=5
x ^=3
print(x)

x=5
x >>=3
print(x)

x=5
x <<=3
print(x)


# In[8]:


x=20
y=15

print("X is equal to Y:",x==y)
print("X is not equal to Y:",x!=y)
print("X is Greater than Y:",x>y)
print("X is Less than Y:",x<y)
print("X is Greater than or equal to Y:",x>=y)
print("X is Less than or equal to Y:",x<=y)


# In[9]:


x=15
print(x>13 and x<20)

x=25
print(x>23 or x<24)

x=35
print(not(x>33 and x<40))


# In[10]:


x=["ahmed","bashir"]
y=["ahmed","bashir"]
z=x

print(x is z)
print(x is y)
print(x==y)


# In[23]:


x=["ahmed","bashir"]
y=["ahmed","bashir"]
z=x

print(x is not z)
print(x is not y)
print(x != y)


# In[12]:


x=["wasim","lubaid","shahroz","usman","faisal","farhan"]
print("faisal"in x)


# In[13]:


x=["wasim","lubaid","shahroz","usman","faisal","farhan"]
print("parkash" not in x)


# In[16]:


import math
#User inputs
velocity = float(input('Give me a velocity to fire at (in m/s):'))
angle = float(input('Give me an angle t fire at:'))
distance = float(input('Give me how far away you are from the structure:'))
height = float(input('Give me the height of the structure(in meters):'))
slingshot = 5 #Height of slingshot in meters
gravity = 9.8 #Earth gravity

#Converting angles to radians
angleRad = math.radians(angle)

#Computing our x and y coordinates
x = math.cos(angleRad)
y = math.sin(angleRad)

#Calculation
time = distance/(velocity * x)
vx =x
vy =y +(-9.8 * time)
finalVelocity = math.sqrt((vx**2)+(vy**2))


# In[50]:


#Question 1(a)
r = 0.5
w = 10
v=r*w
print('The velocity is',v,"m/s")


# In[49]:


#Questin 1(b)
r = 1
w = 10
v=r*w
print('The velocity is',v,"m/s")


# In[48]:


#Question 1(c)
r = 2
w = 10
v=r*w
print('The velocity is',v,"m/s")


# In[31]:


#Question 2(a)
r = 5
w = 523.3
v=r*w
print('The Magnitude of linear velocity',v)


# In[32]:


#Question 2(b)
r = 10
w = 523.3
v=r*w
print('The Magnitude of linear velocity',v,)


# In[47]:


#Question 3
r = 0.3
v = 10
w=v/r
print('The Angular velocity is',w,"rad/sec")


# In[46]:


#Question 4
r = 0.25
v = 10
w=v/r
print('The Angular speed is',w,"m/s**2")


# In[44]:


#Question 5
r = 0.2
w = 12.56
v=r*w
print('The Velocity is',v,"m/s")
t = 10
s=v*t
print('The Distance is',s,"m")


# In[54]:


#Question 6
mile = 50
hour = 60*60
time = 2*60
mile = 1.86*50
m = mile/hour
p = m/1000
a = 0.001241777777778
v = p + a*time
print('The velocity is'),v,"m/s"


# In[ ]:


#Question 7

