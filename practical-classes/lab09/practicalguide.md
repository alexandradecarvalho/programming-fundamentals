## **Programming** Fundamentals, Class 09

### Sets, Comprehensions and Generators

###### this is an adaptation of the practical guide provided by Professor João Manuel de Oliveira e Silva Rodrigues



#### Exercises

1. Using Python in interactive mode, execute the instructions below and interpret the results. Try to predict the results of each expression.

   ```python
   lx = [1,3,5,7,9]
   [10+x for x in lx]
   ly = [2,4,6]
   [x+y for x in lx for y in ly]
   {x+y for x in lx for y in ly}
   [(x,y) for x in lx for y in ly]
   [(x,y) for y in ly for x in lx]
   [x*c for c in "abc" for x in lx]
   [x%3==0 for x in lx]
   [(x,x//3) for x in lx if x%3==0]
   {x:x//3 for x in lx if x%3==0}
   [(x,y) for x in lx for y in ly if x<y]
   {x:[y for y ly if x<y] for x in lx}
   any(x%2==0 for x in lx)
   ```

   

2. The **[imctable2.py](https://github.com/alexandradecarvalho/programming-fundamentals/blob/main/practical-classes/lab09/imctable2.py)** program defines a list with information of names, weights and heights of several people and uses a *list comprehension* to obtain a list with just the names. Substitute the ellipsis by other *list comprehensions* that produce:
   a) A list of BMI values of each person
   b) A list of tuples of people higher than 1.7m
   c) A list of names of the people with BMI between 18 and 25
   
   
3. The **[names.txt](https://github.com/alexandradecarvalho/programming-fundamentals/blob/main/practical-classes/lab09/names.txt)** files has a list of full names of people, with a name per line. Write a program that shows, to each last name, the set of other names found on the list, **without repetitions**. The excerpt below is an example of the wanted result. **Hint:** build a dictionary with key = last name and add the first names to the set associated with each key. This is a problem hardly reduced to a comprehension list.

   > INACIO : {'ROMEU'}
   > SA : {'JOAO'}
   > AMARAL : {'SOLANGE', 'RICARDO'}
   > MONTEIRO : {'RICARDO', 'PAULO', 'BRUNO'}

   

4. Create a `primesUpTo(n)` function that returns a set with all prime numbers until `n`. Use the Sieve of Eratosthenes algorithm: start with the set {2,3,...,n}, then delete the multiples of 2, starting with 2², then the multiples of 3, starting with 3², and you can jump 4 because it has already been deleted (as with all its multiples), then continue eliminating the multiples of each number still in the set. In the end, the set will only have prime numbers.

   ###### (This algorithm can also be implemented over a list of Boolean values, which is an alternative way of representing sets)

5. The **[interests.py](https://github.com/alexandradecarvalho/programming-fundamentals/blob/main/practical-classes/lab09/interests.py)** program has a table (dictionary) with the interests of a set of people. Substitute the ellipsis by adequate expressions in order to:
   a) Create a dictionary with the common interests of each pair of people. So, to each pair of people, it must associate the set of common interests. Notice that if it includes the pair (X,Y) it doesn't include (Y,X).
   b) Find the biggest number of common interests. **Hint:** use the `max` function and a generator expression which goes through the dictionary created in the last indent.
   c) Create a list of pairs of people which have the maximum number of common interests.
   d) Create a list of pairs of people with less than 25% of interest similarity. To measure similarity, use the ***Jaccard index*** between two sets, given by the division between the intersection size and the union size. The expected result is as follows:
   
   > a) Table of common interests:
   > {('Paolo', 'Teresa'): {'music', 'writing'}, ('Frank', 'Maria'): {'writing',
   > 'running'}, ('Marco', 'Teresa'): {'writing', 'music'}, ('Frank', 'Teresa'):
   > {'writing', 'music'}, ('Anna', 'Paolo'): set(), ('Maria', 'Teresa'): {'writing'},
   > ('Anna', 'Frank'): {'reading', 'running'}, ('Frank', 'Paolo'): {'eating', 'music',
   > 'writing'}, ('Anna', 'Marco'): {'reading', 'running'}, ('Frank', 'Marco'):
   > {'reading', 'writing', 'running', 'music'}, ('Marco', 'Maria'): {'writing',
   > 'running'}, ('Anna', 'Maria'): {'running', 'movies'}, ('Marco', 'Paolo'): {'music',
   > 'writing'}, ('Maria', 'Paolo'): {'writing'}, ('Anna', 'Teresa'): set()}
   > b) Maximum number of common interests:
   >
   > 4
   > c) Pairs with maximum number of matching interests: 
