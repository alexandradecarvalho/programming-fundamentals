## Think Python  :snake: 



### :computer: The way of the program :computer:



#### 1. The Python programming language

The most important skill for a computer scientist is **problem solving**: the ability to formulate problems, think creatively about solutions and express a solution clearly and accurately.

**Python is a high-level language**, just like C, C++ and Java. Because computers can only run programs written in **low-level languages**, also called "machine language" or "assembly language", programs in high-level languages need to be processed before they can run. This takes some time, which is a small disadvantage of high-level languages. The advantages are readability (they are much easier to write, read and understand), compactness and **portability** (they can run on different kinds of computer with little or no modifications). 

Two kinds of programs process high-level languages: the **interpreter** and the **compiler**. An interpreter reads the program line by line, executing the commands as they appear. A compiler, however, reads the whole program and fully translates it before the program runs. In this case, the high-level program is called the **source code** and the translated program is called the **object code**, or **executable**.

Python is considered an interpreted language because programs in this language are executed by an interpreter. There are two ways to use the interpreter: **interactive mode** and **script mode**. In interactive mode, a **prompt** appears indicating that the interpreter is ready to receive a Python instruction. After the insertion, the interpreter displays the result. Another way to run Python is to store the code in a file and use the interpreter to execute the contents of a file, which is called a **script**: `python3 filename.py`.



#### 2. What is a program?

A **program** is a sequence of instructions that specifies how to preform a computation, which can be something mathematical (solving a system of equations, finding the roots of a polynomial,...) or something symbolic (searching or replacing text in a document, even compiling a program!,...). 

However complex a program is, every program you have used is made up of: input, output, math, conditional execution and repetitions. So, programming is breaking complex tasks into smaller, simpler subtasks that can be solved using one (or more) of the above five basic instructions - an **algorithm**. 



#### 3. What is debugging?

Programming is error-prone. Programming errors are called **bugs**, and the process of tracking them down is called **debugging**. Three kinds of errors can occur when writing a program: syntax errors, runtime errors and semantic errors.

**Syntax** is the structure of a program and the rules about that structure. Python can only execute a program if its syntax is correct, otherwise the interpreter will display an error message and quit. For example, in Python, parenthesis have to come in matching pairs, so `(1+2)` is legal but `8)` is a **syntax error**.  

The second type of error is a runtime error, also called **exception** because it usually indicates that something exceptional (and bad) has happened, that does not appear until after the program has started running. These are rare to encounter in simple programs. 

**Semantics** refer to the meaning of a program. If there is a semantic error in a program, the program will still run, but it will not do what the programmer wanted it to do. It will do what it was told to do - which can be different. Identifying semantic errors can be tricky because it requires you to work backward by looking at the output of the program and trying to figure out what it is doing.



#### 4. Formal and Natural Languages

**Natural languages** are the ones that people speak, such as Portuguese, or English, that weren't designed by people, but rather evolved naturally. On the contrary, **formal languages** are designed by people for specific applications. Mathematical notation, for example, is a formal language that is particularly good at denoting relationships among number and symbols. Programming languages are formal languages that have been designed to express computations.

Formal languages tend to have strict rules about syntax. One type of syntax rules are regarding to **tokens**, the basic elements of the language, such as words or numbers. The mathematical statement `3 + 3 = $6`  is incorrect because `$` is not a legal token in mathematics. The other type if syntax rules regards the structure of the statement: `3 + = 3` is illegal because even though `+` and `=` symbols are legal tokens, they can't be used one right after the other (in mathematics, not programming! :wink: ). Figuring out the structure of a statement is called **parsing**.



#### 5. The first program

Traditionally, the first program one writes in a new language is a program that only prints "Hello, World!". In Python 3, it looks like this:

```python
print("Hello, World!")
```

The **print statement** is a function that displays a value on the screen. The quotation marks mark the beginning and the end of the function argument, and do not appear in the result.



#### 6. Solved Exercises

##### Exercise 1.1 - Write a well-structured English sentence with invalid tokens in it. Then write another sentence with all valid tokens but with invalid structure.

* Í like the sün. (Í and ü are not valid tokens in English but "I like the sun" is a well-structured sentence)
* Sun me likes. (all valid tokens but invalid structure)

##### Exercise 1.4 - If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile)

```python
>>> 43*60 + 30 # 10 km time in seconds
2610
>>> 2610*1.61 / 10 # 1 mile time in seconds
420.21000000000004
>>> 420.21 / 60 # 1 mile time in minutes 
7.0035
```



### :mega: Variables, expressions and statements :mega:



#### 1. Values and Types

A **value** is one of the basic units of a program. There are different **types** of values: `2` is a whole number, an **integer**, so its type is `int`;  `2.5` is a number with a fractional part but its type is called `float` because these numbers are represented in a format called **floating-point**; and `"Hello, World!"` is a `string`, because it contains a **"string"**  (sequence) of letters. If you are not sure what type a value has, the interpreter can tell you:

```python
>>> type('Hello, World!')
<type 'str'>
>>> type(17)
<type 'int'>
```



#### 2. Variables

One of the most powerful features of a programming language is the ability to manipulate variables. A **variable** is a name that refers to a value. An **assignment statement** creates a new variable and gives it a value:

```python
>>> message = 'And now for something completely different'
>>> n = 17
>>> pi = 3.1415926535897932
```



A common way to represent variables on paper is to write the name with an arrow pointing to the variable’s value. This kind of figure is called a **state diagram** because it shows what state each of the variables is in:

<img src="../img/statediagram.png">



#### 3. Variable names and keywords

To improve readability, variable names are usually chosen so that they can represent what that variable is used for. Variable names can have any number of characters and can contain letters, numbers and underscores (`_`), but they must begin with a letter. It is legal to use uppercase letters, but it is a good idea to begin variable names with a lowercase letter. 

Variable names must not be keywords. **Keywords** are special words used by the interpreter to recognize the structure of the program. Python 3 has 31 keywords:

> and			continue		 except		  if			   	 nonlocal	 	raise			yield
>
> as		   	def			  	 finally	 	  import	 	 not			  	 return
>
> assert		del			   	for 	 		   in			  	 or					try
>
> break	 	elif			   	from	   	  is			  	  pass				while
>
> class		  else				  global		   lambda		 print				with



#### 4. Operators and operands

**Operators** are special symbols that represent computation. The values the operator is applied to are called **operands**.

| Computation    | Operator |
| -------------- | -------- |
| Addition       | +        |
| Subtraction    | -        |
| Multiplication | *        |
| Division       | /        |
| Exponentiation | **       |
| Floor Division | //       |



In Python 3, the result of a division of numbers, even if one or both of the operands or even the result are integers, is a float. **Floor division**, on the contrary, chops off the fraction part, so it only remains the integer part.



#### 5. Expressions and statements

An **expression** is a combination of values, variables and operators. A **statement** is a unit of code that the Python interpreter can execute, including expressions.



#### 6. Interactive mode and script mode

In script mode, an expression, all by itself, has no visible effect. Python actually **evaluates** the expression (retrieves a value by performing the operations on the expression), but it doesn’t display the value unless it is told to. In interactive mode, however, an expression's value is printed. 



#### 7. Order of operations

When more than one operator appears in an expression, the order of evaluation depends on the **rules of precedence**. For mathematical operators, Python follows mathematical convention (**PEMDAS** acronym).



#### 8. String operations

The `+` operator on strings preform **concatenation**, which means joining the strings by linking them end-to-end. For example: `'well' + 'behaved' = 'wellbehaved'`.

The `*` operator also works on strings, preforming repetition. For example: `'good'*3 = 'goodgoodgood'`.



#### 9. Comments

Sometimes, it is a good idea to add notes to a program, to explain them in natural language. These notes are called **comments** and they start with the `#` symbol.  Everything from the `#` to the end of the line is ignored - it has no effect on the program.



#### 10. Solved Exercises

##### Exercise 2.1 - Type the following statements in the Python interpreter to see what they do:

```python
>>> 5
5
>>> x = 5
>>> x + 1
6
```

##### Exercise 2.2 - Assume that we execute the following assignment statements:

```python
width = 17
height = 12.0
delimiter = '.'
```

##### For each of the following expressions, write the value of the expression and the type (of the value of

the expression):

```python
width/2			# 8.5 type float
width/2.0		# 8.5 type float
height/3		# 4 type float
1 + 2 * 5		# 11 type int
delimiter * 5	# '.....' type str
```

##### Exercise 2.3 - Practice using the Python interpreter as a calculator:

##### 1. The volume of a sphere with radius r is 4/3 πr³ . What is the volume of a sphere with radius 5? Hint: 392.7 is wrong!

```python
>>> 4/3*3.14*5**3
523.3333333333334
```

##### 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for

60 copies?

```python
>>> 24.95*0.6 + 3 + 0.75*59
62.22
```

##### 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

```python
>>> 2*8.25 + 3*7.2
38.1
```

**ans:** 5h52 + 0h38m06s = 6h30 am



### :red_circle: Functions :red_circle:



#### 1. Function calls

A **function** is a named sequence of statements which may or may not take arguments and may or may not produce ("return") a result, which is called a **return value**.



#### 2. Type-conversion functions

Python provides built-in functions that convert values from one type to another, just like the `int` function that takes any value and tries to convert it to an integer: `int("32")`.



#### 3. Math functions

Python has a `math` module that provides most of the familiar mathematical functions, like `log` and `sin`. A **module** is a file that contains a collection of related functions. Modules can be used when **imported** first with the **import statement** `import math`. This statement creates a **module object** named "math", which contains the functions and variables defined in the module. 



#### 4. Compositions

One of the most powerful features of programming languages is their ability to take small
programming elements such as variables, expressions and statements, and **compose** them into a useful program. For example, the argument of a function can be an expression including arithmetic operators.



#### 5. Adding new functions

In Python, a programmer can create their own functions. `def` is a keyword that indicates a **function definition**. A function definition specifies the name of a new function (which can only contain letters, numbers and _, but the first character can't be a number) and the argument it takes inside the parentheses. This is called the function **header**, and ends with a colon.

The function definition also specifies the sequence of statements that execute when the function is called - which is indented (by convention with four spaces) and is called the function **body**. 

Once the function is defined, its name then represents a **function object**, which is of the type 'function' and it can be **called** everywhere inside its scope, even inside other functions or itself, by writing its name and, if necessary, its **arguments** inside the parentheses.



#### 6. Definitions and uses

Function definitions get executed just like other statements, but the effect is to create function objects. The statements inside the function do not get executed until the function is called, so the function definition generates no output. So a function needs to be created (defined) before it can be executed (called). 

##### Exercise 3.1 - Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get

```python
Traceback (most recent call last):
  File "think-python.py", line 14, in <module>
    repeat_lyrics()
NameError: name 'repeat_lyrics' is not defined
```



#### 7. Flow of execution

To ensure that the function is defined before it is executed, it is important to know the **flow of execution**, which is the order in which the statements will be executed. Execution always begins from the top of the program to the bottom, one statement at a time. A function call, however, takes the flow of execution on a detour, jumping to the bottom of the function, executing all the statements there, and them coming back to pick up where it left off. When the flow reaches the end of the program, the latter terminates.



#### 8. Parameters and arguments

Inside a function, its arguments are assigned to variables called **parameters**. The name of the variable passed as an argument in the function call has nothing to do with the name of the parameter the function internally converts it to.



#### 9. Variables and parameters are local

When a variable is created inside a function, it is a **local variable**, meaning that it only exists inside the function. If it is called elsewhere, the program won't be able to call it. This is the case with function parameters.



#### 10. Stack diagrams

To keep track of which variables can be used where, it is sometimes useful to draw a **stack diagram**, which shows the value of each variables but also to which function each variable belongs to. Each function is represented by a **frame**, which is a box with the name of the function beside it and the parameters and variables of the function inside it, just like in the following figure: 

<img src="../img/stack.png">



The stack in which the frames are arranged indicates which function called which. If an error occurs during a Python program execution, Python prints the name of the function in which the error occurs and the function that called it, and so on, all the way back to main. This list of functions is called a **traceback**. 



#### 11. Fruitful functions and void functions

Some functions yield results; for lack of a better name, the author calls them **fruitful functions**. Other functions perform an action but don’t return a value. They are called **void functions**. In fruitful functions, one almost always wants to assign the result of the function to a variable and operate over it. In script mode, contrary to interactive mode, if a fruitful function is called on its own, the value is lost!  On the contrary, since void functions don't return a value, if they are assigned to a variable, it gets a special value of type `None`.



#### 12. Why functions?

Functions result in grouping several statements and naming them - making the program easier to read and debug. Functions also make a program smaller by eliminating repetitive code, which enhance maintainability. Functions can also be reused in other programs.



#### 13. Importing with `from`

Python provides two ways to import modules. One of them is: `import math`. This retrieves a module object, in this case named `math`, which contains constants (like `pi`) and functions (like `sin` and `exp`). To use these, one must write it in **dot notation** - the name of the module + dot + the name of the constant/function: `math.pi`.

As an alternative, one can import an object directly from a module: `from math import pi`. Or one can use the star operator to import everything from the module: `from math import *`. 

This way the code can be more concise, but be careful of naming conflicts between imported objects' names and the names of variables/functions in the program.



### :mag: Case study: interface design :mag:



#### 1. Turtle

Turtle is a module that provides a set of functions for drawing lines around the screen. It can be used by importing it: `from turtle import *`. Then, we need to create an **instance** of a Turtle to guide around, and assign it to the variable "bob": `bob = Turtle()` . An instance means a member of a set of objects of the same type - in this case, the type Turtle.



#### 2. Simple repetition

A turtle can, for example, draw a square. One can do this by inserting a statement which makes the turtle draw forward - `bob.forward(100)` - and a statement to turn the turtle around in a square angle - `bob.left(90)` - in a `for` **loop**. It is called a loop because the flow of execution runs through the body of this statement and then loops back to the top and runs it again until the initial conditions aren't met.



#### 3. Encapsulation

Wrapping a piece of code in a function is called **encapsulation**. This allows the naming of a block of code, which can be re-use, making the code more concise than writing the code twice.



#### 4. Generalization

Adapting a function to receive more parameters makes it more general, that's why it's called **generalization**. Because a function with many arguments can become confusing, it is legal and sometimes helpful for readability to include the names of the arguments in the function call. In that case, they are called keyword arguments, and the syntax is as follows: `polygon(bob, n=7, length=70)`.



#### 5. Interface design

The **interface** of a function is a summary of how it is used: what are the parameters? What
does the function do? And what is the return value? An interface is “clean” if it is “as
simple as possible, but not simpler. (Einstein)”



#### 6. Refactoring

**Refactoring** is the process of rearranging a program to improve function interfaces and facilitate reutilization of the code. This often happens because problem comprehension increases while developing a problem and the solution one saw fitted at the beginning may not be considered the best one after getting to know the problem better.



#### 7. A development plan

A **development plan** is the process of writing programs. One of the processes is often "encapsulation and generalization".  The steps are:

1. Start by writing a small program with no function definitions.
2. Once you get the program working, encapsulate it in a function and give it a name.
3. Generalize the function by adding appropriate parameters.
4. Repeat steps 1–3 until you have a set of working functions. Copy and paste working code to avoid retyping (and re-debugging).
5. Look for opportunities to improve the program by refactoring. For example, if you have similar code in several places, consider factoring it into an appropriately general function.

Despite its drawbacks, this process can be useful by allowing the programmer to design the program while coding it.



#### 8. docstring

A **docstring** is a string at the beginning of a function that explains the interface (“doc” is short for “documentation”). In Python, for this we use multiline strings (triple quotes), with a concise explanation of the function's behaviour and its parameters. This kind of documentation is important because if an interface design is hard to explain, it probably needs improving.

​     

###  :twisted_rightwards_arrows: Conditionals and recursion :repeat:



#### 1. Modulus operator

The **modulus operator** works on integers and takes the value of the remainder when the first operand is divided by the second. In Python, it is represented as a percentage sign (%) and it is used between the two integers. 



#### 2. Boolean expressions

A ***boolean* expression** is an expression that takes the values of either `True` or `False`, special values that belong to the type `bool`. These values result, for example, of **relational operators**, like `==`, which compare values. 



#### 3. Logical operators

There are three **logical operators**: `and`, `or` and `not`. `and` is true only if both evaluated conditions are true. `or` is true if either one of the conditions is true. `not` takes the opposite value of the evaluated *boolean* expression.



#### 4. Conditional execution

**Conditional statements** allow the program to change its behaviour depending on some evaluated **condition(s)**. The simplest form of doing this is the `if` statement. This statement has a header (if + condition + semicolon) followed by an indented body. Statements like this are also called **compound statements**. There is no limit for the number of statements in the body, but there has to be at least one. If we have nothing to write there (yet), we can use the `pass` statement.



#### 5. Alternative execution

The if statement can also have a second possible behaviour, in case the first condition is false. This is called **alternative execution** and uses the `else:` syntax. One of the two alternatives (**branches**) is always going to be executed.



#### 6. Chained conditionals

If there are more than two possibilities, more than two branches are needed. So, it is used the **chained conditional** `elif`, which is an abbreviation of "else, if". After `elif`, there is another expression to be evaluated, and then an indented body. There can be unlimited `elif` statements, and the optional `else` statement should always appear at the end. Even if more than one condition is true, only the first true branch executes.



#### 7. Nested conditionals

A conditional statement can be nested inside another. The outer condition contains, then, several branches. In turn, each of these branches could contain other conditional statements. Even though the indentation helps, **nested conditionals** can become hard to read, so they should be avoided. Sometimes they can be avoided by logical operators.



#### 8. Recursion

Just like one function can call another, one function can call itself. This process is called **recursion**. 



#### 9. Stack diagrams for recursive functions

The bottom of the stack, where n=0, is called the **base case** because it does not make a recursive call, so there are no
more frames.

<img src="../img/recursivestack.png">

#### 10. Infinite recursion

If a recursion never reaches a base case, it keeps on making recursive calls forever, so the program never terminates. This is known as **infinite recursion**, and it is generally not a good idea. 



#### 11. Keyboard input

Python3 provides a function so that the function can get input from the keyboard. This function, called `input`, stops the flow of execution until the user types something and presses `Enter`. on never reaches a base case, it keeps on making recursive calls forever, so the program never terminates. This is known as **infinite recursion**, and it is generally not a good idea. 



### :apple: Fruitful functions :pear:



#### 1. Return values

Fruitful functions have a return value, because they have a return statement, which is the `return` keyword followed by an expression or a **temporary variable** created inside the function. Sometimes it is useful to have multiple return statements, one in each branch of a conditional statement.

Fruitful functions have a return value, because they have a return statement, which is the `return` keyword followed by an expression or a **temporary variable** created inside the function. When a function has many branches of a conditional statement, it is a good idea to guarantee that each of them has a `return` statement. In that case, since they are in an alternative conditional, only one will be executed. As soon as a return statement executes, the function terminates without executing any subsequent statements, which, because of never being executed, are called **dead code**.



#### 2. Incremental development

As a program has more and more functions, which in turn become more and more complex, debugging can become hard. One process that can avoid long debugging is **incremental development**, which consists in adding and debugging a small amount of code at a time. To debug a fragment of code built, sometimes, it is needed additional code, like `print` statements, that will later be removed. Using helpful code that is not part of the program is also called **scaffolding**.



#### 3. Composition

Composition is the ability of calling one function inside another.



#### 4. Boolean function

Functions can also return *booleans*, which is often convenient for hiding complicated tests inside functions.



#### 5. Leap of faith

An alternative to following the flow of execution is what the author calls the "leap of faith" - given a function call, we assume that the function works correctly and returns the right result. This is already done when we use built-in functions. 



#### 6. Checking types

The built-in `isinstance` function verifies the type of its argument. Functions like these work as a **guardian**.  This is a programming pattern that uses a conditional statement to check for, and handle, circumstances that might cause an error.



#### 7. Solved Exercises

##### Exercise 6.5 - What happens for larger values of m and n?

```python
RecursionError: maximum recursion depth exceeded in comparison 
```



##### Exercise 6.6 - What happens if you call `middle` with a string with two letters? One letter? What about the empty string, which is written `''` and contains no letters?
In all of the above cases, it is returned an empty string.



###  :arrows_counterclockwise: Iteration :arrows_counterclockwise:



#### 1. Multiple assignment

The same variable can suffer more than one assignment. The new assignment replaces the existing value of that variable for a new one. This is **multiple assignment** and its state diagram can be seen in the following image:<img src="../img/multipleassign.png"> 

#### 2. Updating variables

One of the most common forms of multiple assignment is an **update**, where the new value depends on the old. Before you can update a variable, though, you need to **initialize** it, with a simple assignment. Updating a variable by adding 1 to its old value is called an **increment**, subtracting 1 is called a **decrement**. 



#### 3. The `while` statement

Repetitions, also called **iterations**, are very common in problem solving and programming. One way to iterate is using a `for` statement. Another is the `while` statement, with the following steps:

1. Evaluate the condition, yielding True or False.
2. If the condition is false, exit the while statement and continue execution at the next statement.
3. If the condition is true, execute the body and then go back to step 1.

This type of flow is called a loop because the third step loops back around to the top. The body of the loop should change the value of one or more variables so that eventually the condition becomes false and the loop terminates. Otherwise the loop will repeat forever, which is called an **infinite loop**. 



#### 4. `break`

Sometimes, the condition to be evaluated in order to know if the loop must end only appears halfway through the body. In that case, the `break` statement allows the algorithm to leave the loop. This is common within while loops.



#### 5. Square roots

Loops are often used in programs that compute numerical results by starting with an approximate answer and iteratively improving it. It's the case, for example, of computing square roots with Newton's method. 



#### 6. Algorithms

Newton's method is an example of an algorithm: it is a mechanical process for solving a category of problems.



### :lips: Strings :lips:



#### 1. A string is a sequence

A string is a **sequence** of characters, which can be accessed one at a time with the bracket operator. The integer inside the brackets is called an **index** and it indicates which position of the string we want to access (mind that the first position is index 0). Negative indices count backwards (from the last character to the first).



#### 2. `len`

`len` is a built-in function that returns the number of characters in a string. An empty string has length 0.



#### 3. Traversal with a `for` loop

Sometimes we might need to compute over all characters of string, one at a time. This process is called **traversal** and can be accomplished with a `while` or a `for` loop. 



#### 4. String slices

A segment of a string is called a **slice**, and it can be selected with the bracket operator and two indexes separated by a colon. The first index is inclusive but the last one is exclusive. If the first index is omitted the slice starts at index 0 and if the last index is omitted the slice ends at the end of the word. If the first index is greater than or equal to the second the result is an **empty string**, represented by two quotation marks.



##### Exercise 8.3 - Given that `fruit` is a string, what does fruit[:] mean?

```python
fruit[:] = fruit
```



#### 5. Strings are immutable

Strings are **immutable**, which means we can't assign any new values to its items. An **item** of the string is any of the elements in the sequence of characters.



#### 6. Searching

A **search** is a pattern of computation that traverses a sequence and returns when it finds what we are looking for.



#### 7. Looping and counting

**Counter** is another pattern of computation, which counts the total number of occurrences of a given thing, by looping over something and incrementing each time it finds the wanted result.



#### 8. String methods

A **method** is like a function - it takes arguments and returns a value - but the object we want to apply it to, instead of being an argument inside the brackets, is in the form of dot notation. A method call is called an **invocation**.



#### 9. The `in` operator

The word `in` is a *boolean* operator that takes two strings and returns `True` if the first appears as a substring in the second.



#### 10. String comparison

The relational operators work on strings. In Python, all the uppercase letters come before all the lowercase letters.



#### 11. Solved Exercises



##### Exercise 8.11 -  For each function below, describe what the function actually does

```python
def any_lowercase1(s): # this function determines whether the first character is lowercase
	for c in s:
		if c.islower():
			return True
		else:
			return False
        

def any_lowercase2(s):	# this function always returns True
	for c in s:
		if 'c'.islower():
			return 'True'
		else:
			return 'False'
        
        
def any_lowercase3(s):	# this function determines whether the last character is lowercase
	for c in s:
		flag = c.islower()
	return flag


def any_lowercase4(s):	# this function evaluates if the string contains any lowercase character
	flag = False
	for c in s:
		flag = flag or c.islower()
	return flag


def any_lowercase5(s):	# this function determines if all the characters in the string are lowercase
        for c in s:
            if not c.islower():
                return False
        return True
```



### :mag: Case study: word play :mag:



#### 1. Reading word lists

For this chapter we will use the [words.txt](https://github.com/alexandradecarvalho/programming-fundamentals/tree/main/think-python/words.txt) file, which contains a list of 113 809 official crosswords. Python has a built-in function open that takes the name of a file as a parameter and opens it, returning a **file object**. There are several modes for opening files: `'r'` is for reading the file, `'w'` is for writing.



#### 2. Solved Exercises 

##### Exercise 9.3 - Can you find a combination of 5 forbidden letters that excludes the smallest number of words?

> Probably the vowels: a,e,i,o,u

##### Exercise 9.4 - Can you make a sentence using only the letters "acefhlo"? Other than "Hoe alfalfa"?

> hello, coach alfa fell of alcohol!

##### Exercise 9.5 - How many words are there that use all the vowels "aeiou"? How about "aeiouy"?

> 598 words use "aeiou" and 42 words use "aeiouy"

##### Exercise 9.6 - How many abecedarian words are there?

> There are 596 abecedarian words



#### 3. Search

**Problem recognition** means to recognize a problem as an instance of a previously-solved problem, and applying a previously-developed solution.
