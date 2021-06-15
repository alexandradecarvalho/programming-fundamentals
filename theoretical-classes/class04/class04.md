## Programming Fundamentals, Class 04

###### this is an adaptation of the materials provided by Professor João Manuel de Oliveira e Silva Rodrigues



### Summary

* Functions: definition and invocation
* Parameters and local variables
* Lambda expressions

  

### Functions

* A function definition specifies the name of a new function, a list of parameters, and a block of statements to execute when that function is called

  | Syntax                                        | Example                                            |
  | --------------------------------------------- | -------------------------------------------------- |
  | def function(parameters):<br />    statements | def square(x):<br />    y = x**2<br />    return y |

  

* The first line of the function definition is called the *header*, the rest is called the *body*

* The header starts with the *def* keyword and ends with a colon. The body has to be **indented**

* Function names follow the same rules as variable names



### Definition vs. Invocation

* Do not confuse definition with **function invocation** (aka *function call*)!

  ```python
  def square(x):	# definition
      return x**2
  
  print(square(3))	# invocation
  area = square(size)	# invocation
  h = math.sqrt(square(x2-x1) + square(y2-y1))	# invocations
  ```

  

* In a function **definition** the statements are **not executed**, the are just **stored** for later use

* They are **executed** only if and **when** the function is **invoked**

* A function must be defined before being called

* Define once, call as many times as needed



### Flow of Execution

* Execution always begins at the first statement of a program. Statements are executed one at a time, in order from top to bottom
* Function definitions do not alter the flow of execution of the program. They simply store the statements in the function body for later use. The body is not executed at this time
* A function call is like a detour in the flow of execution. Instead of going to the next statement, the flow jumps to the body of the function, executes all the statements there, and then comes back to pick up where it left off



### Parameters and Arguments

*  Some of the built-in functions we have seen require arguments. For example, when you call `math.sin` you pass a number as an argument

* Some functions take more than one argument: `math.pow` takes two, the base and the exponent

* Inside the function, the arguments are assigned to variables called parameters

  ```python
  def print2times(msg):
      print(msg)
      print(msg)
  ```

  

* This function assigns the argument to a parameter named `msg`. When the function is called, it prints the value of the parameter (whatever it is)



### Return Values

* Some of the functions, such as the `math` functions, produce results

* Other functions, like `print`, perform an action but don't return a value. They are called void functions

* The statement `return expression` exits from a function and returns the result of the expression

* A `return` statement with no argument, return is the same as `return None`

  

### Global vs. Local Variables

* Variables that are defined inside a function body have a local scope, and those outside have a global scope

  ```python
  total = 0	# This is a global variable
  
  def add(a,b):
      total = a + b	# Here total is local variable
      print("Inside the function total: ", total)
      return total
  
  # Now you can call add function
  print(add(10,20))
  print("Outside the function global total: ", total)
  ```

  

* Parameters are local variables too

  

### Keyword Arguments

* In a **function call**, *positional arguments* are assigned to parameters according to their position

  ```python
  def printinfo(name,age):
      print("Name:", name)
      print("Age: ", age)
      
  printinfo("miki", 50)	# "miki" = name and 50 = age
  ```

  

* When you use **keyword arguments**, the caller identifies the arguments by the parameter name

  ```python
  printinfo("miki", age=50)
  printinfo(age=50, name="miki")
  ```

  

* With keyword arguments you don't have to remember the order of parameters, just their names

  

### Default Argument Values

* A **function definition** may specify default argument values for some of its parameters

```python
def printinfo(name, age=35):
    print("Name: ", name)
    print("Age: ", age)
```



* When calling the function, if a value is not provided for that argument, it takes the default value

```python
printinfo("miki", 50)
printinfo("miki")	# here, age is 35!
printinfo(name="miki")	# same here
```



### Variable-length Arguments

* You may need to process a function for more arguments than you specified while defining the function
* These arguments are called variable-length arguments and are not named in the function definition

```python
def printinfo(arg1, *vartuple):
    print(arg1)
    for var in vartuple:
        print(var)
        
printinfo(10)
printinfo(70,60,50)	# the last two are passed as a tuple
```

```python
X and Y # if X is false then X, otherwise Y
X or Y # if X is true then X, otherwise Y
```



* An asterisk is placed before the variable name that holds the values of all non-keyword variable arguments



### Lambda Expressions

* A *lambda expression* is an expression whose result is a function

* You may store it in a variable and use it later, for example

  ```python
  add = lambda a,b: a + b	# lambda expression
  # Now you can call add as a function
  print("Total: ", add(20,10))	# Total: 30
  ```

  

* They're also known as *anonymous functions*

* Lambda forms can take zero or more parameters, but return a single result

* They cannot contain statements, only a single expression

* They're most useful to pass as arguments to other functions
