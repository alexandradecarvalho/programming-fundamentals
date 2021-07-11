## **Programming** Fundamentals, Class 11

### Recursion

###### this is an adaptation of the practical guide provided by Professor João Manuel de Oliveira e Silva Rodrigues



#### Exercises

1. The **[recErrors.py](https://github.com/alexandradecarvalho/programming-fundamentals/blob/main/practical-classes/lab11/recErrors.py)** program defines two recursive functions, which are both wrong: they don't end. In both cases, try to detect the cause and fix the mistake. **Hint:** confirm if the functions satisfy the termination conditions.

3. In the **[genWords.py](https://github.com/alexandradecarvalho/programming-fundamentals/blob/main/practical-classes/lab11/genWords.py)** file, the `genWords3` function generates a list with all words of length 3 that can be made up off of some characters, chosen from a given list of symbols. Write a general version, `genWords`, that generates all words of length `n`. Get a list of words of size n-1 and, to each of them, add each symbol of the alphabet. What will the base case be? And what is its result?
   
3. In the **[findFiles.py](https://github.com/alexandradecarvalho/programming-fundamentals/blob/main/practical-classes/lab11/findFiles.py)**, create a `findFiles` function that returns a list with the names of all files with a given extension in a given directories. The search must go through the directory and recursively through all its subdirectories. That program also has a pre-made function that shows the contents of a directory, recursively. Analyse it.

