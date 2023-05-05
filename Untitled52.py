#!/usr/bin/env python
# coding: utf-8

# Create a function that takes a list of non-negative integers and strings and return a new list without the strings.

# In[15]:


def filter_list(lst):
    return [x for x in lst if type(x) == int]


# In[16]:


filter_list([1, 2 , "a", "b"])


# In[17]:


filter_list([1, "a", "b", 0, 15])


# In[18]:


filter_list([1, 2, "aasf", "1", "123", "123"])


# The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.
# 

# In[39]:


def reverser(string):
    reversed_string = string[::-1]
    result =''
    for char in reversed_string:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result


# In[40]:


reverser("Hello World")


# In[41]:


reverser("ReVeRsE")


# In[42]:


reverser("Radar")


# You can assign variables from lists like this:
# lst = [1, 2, 3, 4, 5, 6]
# first = lst[0]
# middle = lst[1:-1]
# last = lst[-1]
# 
# print(first) ➞ outputs 1
# print(middle) ➞ outputs [2, 3, 4, 5]
# print(last) ➞ outputs 6
# With Python 3, you can assign variables from lists in a much more succinct way. Create variables first, middle and last from the given list using destructuring assignment (check the Resources tab for some examples), where:
# first  ➞ 1
# 
# middle ➞ [2, 3, 4, 5]
# 
# last ➞ 6
# Your task is to unpack the list writeyourcodehere into three variables, being first, middle, and last, with middle being everything in between the first and last element. Then print all three variables.
# 

# In[44]:


lst =[1,2,3,4,5,6]
first = lst[0]
middle = lst[1:-1]
last = lst[-1]


# In[45]:


print(first)


# In[47]:


print(middle)


# In[48]:


print(last)


# Write a function that calculates the factorial of a number recursively.
# 

# In[49]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# In[50]:


factorial(5)


# In[51]:


factorial(3)


# In[52]:


factorial(1)


# In[53]:


factorial(0)


# Write a function that moves all elements of one type to the end of the list.
# 

# In[56]:


def move_to_end(lst, element_type):
    filtered_lst = [x for x in lst if type (x) != element_type]
    element_lst = [x for x in lst if type (x) ==element_type]
    return filtered_lst + element_lst


# In[57]:


move_to_end([1, 3, 2, 4, 4, 1], 1)


# In[58]:


move_to_end([7, 8, 9, 1, 2, 3, 4], 9)


# In[59]:


move_to_end(["a", "a", "a", "b"], "a")


# In[ ]:




