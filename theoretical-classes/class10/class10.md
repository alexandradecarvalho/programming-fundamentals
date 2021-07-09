## Programming Fundamentals, Class 10

###### this is an adaptation of the materials provided by Professor João Manuel de Oliveira e Silva Rodrigues



### Summary

* List comprehensions
* Dictionary and set comprehensions
* Generator expressions



### Building Lists

* Quite often, we need to **create lists** with elements **related to** those in **another list**
* For example: return a list of the squares of the values in lst

```python
lst = [1, -3, 2]
lst2 = []			# init result with empty list
for v in lst:		# loop over original list:
    v2 = v ** 2		# compute a new value
    lst2.append(v2)	# append it to result
print(lst2)			#-> [1,9,4]
```



* Another example: return a list of uppercase versions of the strings in list
  * what do you need to change?
* These programs always follow the **same** basic **pattern**



### List Comprehensions

* Python provides a more concise way to produce such lists:

```python
nums = [4,-5,3,7,2,3,1]
nums2 = [v**2 for v in nums]				#-> [16,25,9,49,4,9,1]
args = ['apple','dell','ibm','hp','sun']	
args2 = [s.upper() for s in args]			#-> ['APPLE','DELL','IBM','HP','SUN']
```



* These are **list comprehensions**: **expressions** that generate lists by operating on the elements of other collections
* The `for...in` clause is part of the expression - it is not a statement
* List comprehensions may also include `if` clauses: `args3 = [s.upper() for s in args if len(s) > 3] #-> ['APPLE','DELL']`
* List comprehensions may include multiple `for...in` and if clauses: `[(a,b) for a in [1,2] for b in nums if b > 3] #-> [(1,4), (1,7), (2,4), (2,7)]`



### Dictionaries and Set Comprehensions

* We may also create dictionaries by comprehension:

```python
args = ['apple','dell','ibm','hp','sun']	
{a: len(a) for a in args}					#-> {'apple':5,'ibm':3,'hp':2,...}
```



* Other variations are possible too, of course
* Sets may also be defined by comprehension: `s = {2+x for x in [3,4,5,4]}`



### Generator Expressions

* **Generator expressions** are identical to the expressions used in list comprehensions, but enclosed in `()`
* They create an object that generates items only ***if and when needed***, unlike list comprehensions - this strategy is called *lazy evaluation*
* They are convenient as arguments to some functions:

```python
nums = [4,-5,3,7,2,3,1]
sum(x/2 for x in nums if x%2==0)	#-> 3.0
all(x>0 for x in nums)				#-> False
```



* We may use **generator expressions** to create other types of sequences, for example: `tuple(v for v in nums if v<3) #-> (-5,2,1)`
