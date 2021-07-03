## Programming Fundamentals, Class 07

###### this is an adaptation of the materials provided by Professor João Manuel de Oliveira e Silva Rodrigues



### Summary

* Files
* Command Line Arguments
* Exceptions and Assertions



### Text Files

* Most of the programs we have seen so far are transient in the sense that they run for a short time, take input and produce output, but when they end, everything disappears

* One of the simplest ways for programs to maintain their data is by reading and writing text files

* A text file is a sequence of characters stored on a persistent medium like a hard drive, flash memory, or CD-ROM

* Characters are encoded in bytes according to a standard coding table such as UTF-8 or ASCII, for instance

  

### Opening and Closing Files

* We must prepare a file before reading and writing. This is called **opening** the file
* The built-in function `open` takes the name of the file and returns a file object that we can use to access it

```python
fileobj = open(file_name, 'r')	# open for reading
fileobj = open(file_name, 'w')	# open for writing
```



* More modes: 'r', 'w', 'a', 'r+', 'w+', 'a+', 'rb'...
* After using the file, remember to **close** it: `fileobj.close()`
* The `with` statement will **automatically close** files

```python
with open(file_name, mode) as fileobj:
	statement to read/write fileobj
# fileobj.close not required!
```



### Text *versus* Binary Mode

* Normally, files are opened in ***text mode***. This means:
  * You read/write *strings* of characters (type `str`)
  * Characters are *encoded*: one character may use several bytes  (the encoding may be specified with the encoding = `optional` argument)
  * Platform-specific *line endings* are converted to/from `\n`
* For files that don't contain text, you should use '`rb`' or '`wb`' to open in ***binary mode***. This means:
  * You read/write strings of *bytes* (type `bytes`, not `str`)
  * No conversions occur



### Reading a File

* We can use a `for` loop to read a file *line by line*

```python
fin = open('words.txt')
for line in fin:	# for each line from the file
	print(line)		# do something with it
fin.close()
```



* Another way is using the `readline` method 

```python
while True:
    line= fin.readline()	# returns line to the end
	if line == "": break	# empty means end-of-file
	print(line)		
```



* We can also read the entire file as string: `text = fin.read()	# read as much as possible (up to EOF)`
* Or read at most N characters: str = `fin.read(10) # read upto 10 chars (empty means EOF)`



### Moving the File Cursor

* We generally read and write sequentially, from start to end

* But sometimes we need to "jump" around

* The `tell()` method tells you the current position within the file

* The `seek(offset)` method changes the current file position to `offset` bytes from the start (an optional argument can specify a different reference point)

```python
a0 = f.readline()	# read a line
pos ⁼ f.tell()		# store position
a1 = f.readline()	# read second line
f.seek(pos)			# return the stored position
a2 = f.readline()	# read second line again (a2 == a1)
```



### Write to a File

* To write to a file, open it with mode '`w`' (or '`a`'): `fout = open('output.txt','w')`
* Opening it in '`w`' mode creates a **new file** or *truncates* an existing one, *i.e.* it **deletes** the old data and starts from scratch
* The `write` method puts data into the file:

```python
line1 = 'To be or not to be, \n'
fout.write(line1)
```



* Again, the `file` object keeps track of where it is, so if you call `write` again, it adds the new data to the end: 

```python
line2 = 'That is the question.\n'
fout.write(line2)
```



* The argument of write has to be a string, so we have to convert other types of values:

```python
x = 0.75
fout.write('X: ' + str(x))
```



* Or use the string format method: `fout.write('{s:} costs {:.2f}€.'.format('coffee',x))`
* You may also use `print` with the `file=` argument:

```python
print('X: ',x, file=fout)
print('{:s} costs {:.2f}€.'.format('coffe',x), file=fout)
```



* When you are done writing, remember to close the file! `fout.close() # OR use the with statement`



### Filenames and Paths

* The `os` module provides functions for working with files and directories ("`os`" stands for "operating system")
* `os.getcwd()` returns the name of the current directory
* A string that identifies a file is called a ***path***
* An **absolute path** starts with `/` (the topmost directory)
* A **relative path** starts from the current directory
* To find an absolute path to a file, you can use: `os.path.abspath(path)`
* There are functions to check existence and type of files:
  * `os.path.exists(f)` checks whether a file exists
  * `os.path.dir(f)` checks whether a filename is a directory
  * `os.path.isfile(f)` checks whether it's a regular file
* And a function to get the contents of a directory:
  * `os.listdir` returns a list of the files (and other directories) in the given directory
  * backward from the end



### Command Line Arguments

* The Python `sys` module provides access to any command-line arguments via the `sys.argv`:
  * `sys.argv` is the list of command-line arguments
  * `len(sys.argv)` is the number of command-line arguments
  * `sys.argv[0]` is the program (script) name

```python
import sys
print('Number of args: ', len(sys.argv), ' arguments.')
print('Argument list: ', sys.argv)
```



* Running the above script as `python3 test.py arg1 arg2 arg3` produces:

```python
Number of args: 4 arguments.
Argument list: ['test.py','arg1','arg2','arg3']
```



### Exceptions

* Python provides an important feature to handle any unexpected events in your program: **exceptions**
* You've seen exceptions before:

```python
int("one")	#-> ValueError: invalid literal for int()
open("foo")	#-> FileNotFoundError: No such file...
```



* When Python encounters a situation that it cannot cope with, it ***raises*** an exception
* That **interrupts** the normal flow of the execution: the current function is interrupted, then the one that called it, etc., until the main program itself is interrupted
* Information about the event is transmitted all the way through in an *exception object*



### Handling Exceptions

* You can intercept selected exceptions and recover normal execution with the `try` statement:

```python
try:
    fh = open('testfile', 'r')
    fh.read()
except IOError:
    print('Error: can\'t find file or read data')
else:
    print('Written content in the file successfully')
    fh.close()
```



* The `except` statement can also be used with no exceptions or with more than one



### Exception Information

* An exception can have an *argument*, which is a value that gives additional information about the problem:

```python
def temp_convert(var):
    try:
        return int(var)
    except ValueError as x:
        print('Not numeric\n', x)

temp_convert("xyz")
```



### Raising Exceptions

* We can raise exceptions (of any type) by using the raise statement

  ```python
  def functionName(level):
  	if level <1:
  		raise Exception(level)
      # code here is not executed if we raise the exception
      return level
  
  try:
  	v = functionName(-10)
  	print("level = ", v)
  except Exception as e:
  	print("error in level argument", e.args[0])
  ```



### Assertions

* An **assertion** is a condition that we know (or require) to be true at some point in a program
* Use the `assert` statement for checking assertions
* It evaluates the condition and, if false, raises an exception
* We can turn off assertion checking when we are done with testing of the program (call Python with -o flag)
* We can place assertions at the start of a function to check for valid input, or after a function call to check for valid output:

```python
def KelvinToFahrenheit(temperature):
	assert temperature >= 0, "Colder than absolute zero!"
	return ((temperature-273)*1.8)+32

print(KelvinToFahrenheit(-5))	#-> AssertionError: Colder than absolute zero!
```