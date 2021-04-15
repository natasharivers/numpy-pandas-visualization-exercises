#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#MATPLOTLIB EXERCISES:


# In[ ]:


# 1 Use matplotlib to plot the following equation:

#y=x2−x+2
#You'll need to write the code that generates the x and y points.

#Add an anotation for the point 0, 0, the origin.


# In[ ]:


import matplotlib.pyplot as plt
import math
import numpy as np


# In[ ]:


x= range(-50,50)
y = [n **2 - n+2 in x]


# In[ ]:


plt.scatter(x,y)
plt.title('y = $x^2$ - x+2')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.annotate('origin', xy= (0,0))
plt.show()


# In[ ]:


#2nd way of doing #1


# In[ ]:


x =np.array(range(100))
y = x**2 - (x+2)


# In[ ]:


plt.plot(x,y)
plt.title('y = $x^2$ - x+2')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.annotate('origin', xy= (0,0))
plt.show()


# In[ ]:


#2 Create and label 4 separate charts for the following equations (choose a range for x that makes sense)
#2.a: y=√x
 
x= np.array(range(100))
y1 = [math.sqrt(x) for x in x]
plt.plot(x,y)
plt.title('y=√x')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()


# In[ ]:


#2 Create and label 4 separate charts for the following equations (choose a range for x that makes sense)
#2.b: y=x**3
 
 
x= range(-50,50)
y = [n **3 for n in x]
plt.plot(x,y)
plt.title('y = $x^3$')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()


# In[ ]:


#2 Create and label 4 separate charts for the following equations (choose a range for x that makes sense)
#2.c: y=2**x

x= np.array(range(100))
y = 2**x
plt.plot(x,y)
plt.title('y = $2^x$')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()
 


# In[ ]:


#2 Create and label 4 separate charts for the following equations (choose a range for x that makes sense)
#2.d: y=1/(x+1)

 
x= np.array(range(100))
y= 1/(x+1)
plt.plot(x,y)
plt.title('y = $1/(x+1)$')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()


# In[ ]:


#3 Combine the figures you created in the last step into one large figure with 4 subplots.

x= np.array(range(100))
y1 = [math.sqrt(x) for x in x]
y2 = [x **3 for x in x]
y3 = [2**x for x in x]
y4= [1/(x+1) for x in x]


# In[7]:


plt.figure(figsize = (12,10))

plt.suptitle('Separate Charts')

plt.subplot(2, 2, 1)
plt.plot(x,y1, color = 'orange')
plt.title('y1 = $√x$')

plt.subplot(2,2,2)
plt.plot(x,y2, color = 'g') 
plt.title ('y2 = $x^3$')


plt.subplot(2,2,3)
plt.plot(x,y3, color = 'm') 
plt.title ('y3 = $2^x$')


plt.subplot(2,2,4)
plt.plot(x,y4, color= 'black') 
plt.title ('y4 = $1/(x+1)$')

plt.tight_layout()

plt.show()


# In[ ]:


#4 Combine the figures you created in the last step into one figure 
#where each of the 4 equations has a different color for the points. 
#Be sure to include a legend and an appropriate title for the figure.


# In[4]:


import matplotlib.pyplot as plt

import math as math

import numpy as np

import pandas as pd


# In[5]:


x= list(range(5))
y1 = [math.sqrt(x) for x in x]
y2 = [x **3 for x in x]
y3 = [2**x for x in x]
y4= [1/(x+1) for x in x]


# In[8]:


plt.figure(figsize =(10,8))

plt.suptitle('Separate Charts')


plt.plot(x, y1, color = 'orange', label = 'y1 = $√x$')
plt.plot(x, y2, color = 'green', label = 'y2 = $x^3$')
plt.plot(x, y3, color = 'm', label = 'y3 = $2^x$')
plt.plot(x, y4, color = 'black', label = 'y4 = $1/(x+1)$')

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.grid(True, ls= '--')

plt.legend()


# In[ ]:




