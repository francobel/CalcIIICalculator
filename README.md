# Vector Calculus Calculator

To run the application

	$ python calc.py

This is a desktop application that is aimed to help anyone that's currently enrolled in a Calculus 3 course and would like to have an all in one tool handy. This project has 3 main sections:

	Vector Algebra
	Differential Operators
	Derivates

### Vector Algebra ###
The vector algebra section is compromised of 5 tools:

	1. Vector Addition
	2. Vector Subctraction
	3. Scalar Multiplication
	4. Dot Product
	5. Cross Product

These tools will generally have 1 or 2 empty fields for you fill in with vectors.
The input should be in **ORDER SET NOTATION**:

	ex: (1,2,3)

At this point in time the tools only work with integers. Float interaction will come in the future. 

### Differential Operators ###
The differential operators section comes with 3 tools:

	1. Gradient
	2. Divergence
	3. Curl
	
For all of the differential operator tools you will get an empty field in which you will input whatever corresponds to the operation you have selected. Ultimately you will have to input functions in some way or another. At the moment you have to enter your function in a very unconventional way, if I have time later I might change it. There's three unconventionalities:

	- Your variables should be lower case or they wont work.
	- You have to explicitly represent your multiplications with an asterisk.
	- When you want to raise to a power, instead of using a caret '^' you will use a double 
	  asterisk '**'.

	What you would normally write in your math class as: 2X^2+3Y+3
        	                         Should be input as: 2*x**2+3*y+3

**Gradient:**

For the gradient tool you have to enter a function into the empty field.

When you take the gradient of a function you take the partial derivative of it with respect to x, y and z and form a vector field with the results of the partial derivation. 

A function ends up yielding a vector field.

**Divergence:**

For the divergence tool you have to enter a vector field. A vector field is basiacally 3 functions joined together in order set notation.
	
	ex: (x**2+1, 3*y, z**3+5)

When you take the divergence of a vector field you end up taking the partial derivative with respect to x of the first function, the partial derivative of y with respect to the second function and the partial of the last with respect to z. After that you add up all of the results and that is your gradient. 

A vector field ends up yielding a function.

**Curl:**

For the curl tool you have to enter a vector field. The same regulations as above apply.

When you take the curl of a vector field you end up taking the cross product of it with the del operator. 
This should yield you another vector field.

### Derivatives ###

The derivatives section comes with 2 tools: 

	1. Derivative
	2. Partial Derivative
	
The tools are pretty self explanatory. You enter a function and either its derivative or partial derivative will be returned.
For guidelines on how to enter functions look at the differential operators section.


