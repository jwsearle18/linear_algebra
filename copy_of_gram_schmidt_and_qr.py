# -*- coding: utf-8 -*-
"""Copy of Gram_Schmidt_and_QR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AbULL80GX4R6gdFAlrXbxh5zzj7ViBZH

#**Lab 12 - Gram-Schmidt and QR decompositions**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab12"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="JADEN"

last_name="SEARLE"

# Enter your Math 215 section number in between the quotation marks.

section_number="Your Math 215 section number goes here"

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER!

BYUNetID="JADENWS"

"""**Import NumPy**"""

import numpy as np

"""**Problem 1**"""

#This function reads in two vectors and outputs a boolean variable describing whether the two vectors are orthogonal.

def orthogonal_check(a,b):
  dot_product = np.dot(a, b)

  cutoff = 1e-12
  return np.abs(dot_product) < cutoff

u = np.array([1, 2, -1, 4])
v = np.array([2, -2, -6, -1])
x = np.array([1, 1, 1])
y = np.array([1, 1, 2])

print(orthogonal_check(u, v))
print(orthogonal_check(x, y))

"""Check your function:"""

a=np.array([1,2,-1,4])
b=np.array([2,-2,-6,-1])

orthogonal_check(a,b)

"""**Problem 2**"""

# This function reads in a list of vectors and checks whether they form an orthogonal set. Orthcheck should be a Boolean value (True or False).

def orth_set_check(vect_set):
  for i in range(len(vect_set)):
      for j in range(i + 1, len(vect_set)):
          if not orthogonal_check(vect_set[i], vect_set[j]):
              return False
  return True

L1 = [np.array([1, -1, 0]), np.array([1, 1, 1]), np.array([0, 1, -1])]
L2 = [np.array([1, 0, 0]), np.array([0, 2, 0]), np.array([0, 0, 3])]

print(orth_set_check(L1))
print(orth_set_check(L2))

"""Check your function:"""

p=[np.array([1,-1,0]),np.array([1,1,1]),np.array([0,1,-1])]
q=[np.array([1,0,0]),np.array([0,1,0]),np.array([0,0,1])]

orth_set_check(p)

"""**Problem 3**"""

# This function accepts a vector and returns a unit vector in the same direction.

def normalize(v):
  magnitude = np.linalg.norm(v)

  unit_vector = v / magnitude

  return unit_vector

"""Check your function:"""

normalize(np.array([1,1,1,1]))

"""**Problem 4**"""

# This function accepts two vectors a and b and returns the projection of a onto b.

def proj(a,b):
  dot_product = np.dot(a, b)

  b_dot_b = np.dot(b, b)

  proj_a_b = (dot_product / b_dot_b) * b

  return proj_a_b

"""Check your function:"""

a=np.array([1,4,1])
b=np.array([1,1,1])
proj(a,b)

"""**Problem 5**"""

# This function accepts a list of linearly independent vectors V, and produces a new list X of orthonormal vectors which span the same space as a the vector of V.

def gram_schmidt(V):
  X = V.copy()
  n = len(V)

  for i in range(1, n):
      for j in range(i):
          X[i] = X[i] - proj(X[i], X[j])

  for i in range(n):
      X[i] = normalize(X[i])

  return X

"""Check your function:"""

L=[np.array([1,3,2,4,0]),np.array([-1,0,4,5,0]),np.array([0,2,2,2,2]),np.array([3,2,3,2,0])]
A=gram_schmidt(L)
print(orth_set_check(A))
A

"""**Problem 6**"""

# This function accepts a matrix A as a 2D NumPy Array, and returns two new matrices Q and R.

def QR_decomposition(A):
  columns = [np.array(A[:, j]) for j in range(A.shape[1])]

  Q_columns = gram_schmidt(columns)

  Q = np.column_stack(Q_columns)

  R = np.dot(Q.T, A)

  return Q, R

"""Check your function:"""

A=np.transpose(np.array([[1,3,2,4,0],[-1,0,4,5,0],[0,2,2,2,2],[3,2,3,2,0]]))
np.shape(A)[1]
Q,R=QR_decomposition(A)

print(Q)
print(R)

"""We can check to see if QR=A, after rounding with the following command:"""

np.round(np.matmul(Q,R))

"""**Problem 7**"""

# This Function was created in Lab 5.  It accepts an upper triangular square matrix U and a vector b, solves Ux=b for x.  You may use it in the function QR_solver.

def back_substitution(U,b):
  n=len(b)
  x=np.array([0.0 for i in range(n)])
  for i in range(n-1,-1, -1):
    r=(b[i]-sum([x[j]*U[i][j] for j in range(i+1,n)]))/U[i][i]
    x[i]=r
  return x

# This function accepts an invertible matrix A and a vector b, solves Ax=b for x.

def QR_solver(A,b):
  Q, R = QR_decomposition(A)

  Qt_b = np.dot(Q.T, b)

  x = back_substitution(R, Qt_b)

  return x

A=np.array([[3,1,-2],[1.5,2,-5],[2,-4,1]])
b=np.array([1.1,3,-2])
QR_solver(A,b)

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to [gradescope.com](https://gradescope.com) for grading.
"""