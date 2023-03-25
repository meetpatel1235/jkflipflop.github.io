#!/usr/bin/env python
# coding: utf-8

# In[1]:


def OR(A, B):
	return A | B	

print("Output of 0 OR 0 is", OR(0, 0))
print("Output of 0 OR 1 is", OR(0, 1))
print("Output of 1 OR 0 is", OR(1, 0))
print("Output of 1 OR 1 is", OR(1, 1))


# In[2]:


def AND(A, B):
	return A & B	

print("Output of 0 AND 0 is", AND(0, 0))
print("Output of 0 AND 1 is", AND(0, 1))
print("Output of 1 AND 0 is", AND(1, 0))
print("Output of 1 AND 1 is", AND(1, 1))


# In[1]:


def NOT(A):
	return ~A+2	

print("Output of NOT 0 is", NOT(0))
print("Output of NOT 1 is", NOT(1))


# In[2]:


# Function to simulate AND Gate
def AND(A, B):
	return A & B;	

# Function to simulate NOT Gate
def NOT(A):
	return ~A+2	

# Function to simulate NAND Gate
def NAND(A, B):
	return NOT(AND(A, B))


print("Output of 0 NAND 0 is", NAND(0, 0))
print("Output of 0 NAND 1 is", NAND(0, 1))
print("Output of 1 NAND 0 is", NAND(1, 0))
print("Output of 1 NAND 1 is", NAND(1, 1))


# In[3]:


def OR(A, B):
	return A | B;	

# Function to simulate NOT Gate
def NOT(A):
	return ~A+2	

# Function to simulate NOR Gate
def NOR(A, B):
	return NOT(OR(A, B))


print("Output of 0 NOR 0 is", NOR(0, 0))
print("Output of 0 NOR 1 is", NOR(0, 1))
print("Output of 1 NOR 0 is", NOR(1, 0))
print("Output of 1 NOR 1 is", NOR(1, 1))


# In[4]:


def XOR(A, B):
	return A ^ B

print("Output of 0 XOR 0 is", XOR(0, 0))
print("Output of 0 XOR 1 is", XOR(0, 1))
print("Output of 1 XOR 0 is", XOR(1, 0))
print("Output of 1 XOR 1 is", XOR(1, 1))


# In[5]:


def XOR(A, B):
	return A ^ B

# Function to simulate NOT Gate
def NOT(A):
	return ~A+2	

# Function to simulate XNOR Gate
def XNOR(A, B):
	return NOT(XOR(A, B))


print("Output of 0 XNOR 0 is", XNOR(0, 0))
print("Output of 0 XNOR 1 is", XNOR(0, 1))
print("Output of 1 XNOR 0 is", XNOR(1, 0))
print("Output of 1 XNOR 1 is", XNOR(1, 1))


# In[6]:


def AND(a,b,c): 
 return a&b&c
 
def OR(a,b): 
 return a|b
def NOT (a):
 return int(not a)
def NOR(a,b): 
 ans = OR(a,b)
 return NOT(ans)
j = int(input("Enter value of J = "))
k = int(input("Enter value of K = "))
Qp = int(input("Enter value of Previous Output = "))
r = AND(k,Qp,1)
s = AND(j,NOT(Qp),1)
a1 = NOR(s,Qp)
Qn = NOR(r,a1)
print("value of Next Output is = ",Qn)


# In[7]:


def AND(a,b,c): 
 return a&b&c
 
def OR(a,b): 
 return a|b

def NOT (a):
 return int(not a)
def NOR(a,b): 
 ans = OR(a,b)
 return NOT(ans)
S = int(input("Enter value of S = "))
R = int(input("Enter value of R = "))
Qp = int(input("Enter value of Previous Output = "))
a1 = AND(R,1,1)
a2 = AND(S,1,1)
if(a1 == a2 == 1):
 print("value of Next Output is = Intermediate")
else:
 a3 = NOR(a2,Qp)
 Qn = NOR(a1,a3)
 print("value of Next Output is = ",Qn)


# In[8]:


def AND(a,b,c): 
 return a&b&c
 
def OR(a,b): 
 return a|b
 
def NOT (a):
 return int(not a)
def NOR(a,b): 
 ans = OR(a,b)
 return NOT(ans)
D = int(input("Enter value of D = "))
R = NOT(D)
Qp = int(input("Enter value of Previous Output = "))
a1 = AND(R,1,1)
a2 = AND(D,1,1)
a3 = NOR(a2,Qp)
Qn = NOR(a1,a3)
print("value of Next Output is = ",Qn)


# In[ ]:




