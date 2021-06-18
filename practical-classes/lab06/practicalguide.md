## **Programming** Fundamentals, Class 06

### Sequences

###### this is an adaptation of the practical guide provided by Professor João Manuel de Oliveira e Silva Rodrigues



#### Exercises

1. Try to guess the result of each of the following instructions. Some of them don't have a result and others throw errors. Use Python in interactive mode to confirm.

   ```python
   lst = [5,3,8,7]
   len(lst)
   lst[2]
   lst[4]
   lst[-4]
   lst[1:3]
   lst[:-1]
   lst[2:2]
   lst[2:2] = [99] ; lst
   lst.append(33) ; lst
   
   t = ("ana", (1974,4,25))
   len(t)
   t[1]
   t[1][0]
   (1974,3,30) < (1974,4,1)
   (1974,3) < (1974,3,-1,-2)
   s = "abcde"
   s[2:] + s[:2]
   s[1::2]
   s > "abel"
   ```

   

2. Follow these steps, testing each of them:

   a) Create the `inputFloatList()` function which reads a sequence of numbers inputed by the user and returns them in a list. The user must introduce one number per line and indicate the end with an empty line.

   b) Create the `countLower(lst, v)` function which calculates and returns the number of `lst`'s elements that are lower than `v`.

   c) Create the `minmax(lst)` function which returns the maximum and the minimum values of a list. Can you do it without the `min` and the `max` functions?

   d) Use the function above to create a program which reads a list of numbers, determines the average between the maximum and the minimum values and that counts how many numbers are inferior to that value. 

3. The program **[telephone.py](https://github.com/alexandradecarvalho/programming-fundamentals/blob/main/practical-classes/lab06/telephone.py)** defines two lists, one with telephone numbers and other with the correspondent names.

   a) Complete the `telToName` function so that, given a phone number (and both lists), it can return the right name (or the number if it's not on the list). This is what phones do when they get an incoming call.

   b) Complete the `nameToTels` function so that, given part of a name, it can return the list of the matching numbers for names that include the searched part (just like when you search through a phone list).

   c) Run the program to test these functions.

4. Write a function that, given a list of football teams, generates a list of all matches that can be done. With 3 teams you should get 6 matches and with 4 teams you should get 12 matches. Confirm and test with even more teams.

5. Write a function that counts how many digits appear in a given string: `countDigits("23 mil 456")` should return `5`. **Hint:** the method `isdigit` verifies if a string only has digits.

6. Write a function that, given a name, creates a short version, formed only by the capital letters: `shorten("Universidade de Aveiro") = "UA"`. **Hint:** the `isupper` method verifies if a string only has capital letters.

7. Write a `ispalindrome(s)` function that returns a `boolean` value indicating whether or not the string is a palindrome.

8. Resolve the exercises below:

   a) Write a function that, given a string, returns another one, made up by all characters of even positions followed by all characters of odd positions of the first string. For example, `evenThenOdd("abcd")` should return "`acbd`". You can do this using slicing and concatenation. 

   b) Write a function that, given a string s, returns a similar string but without duplicate adjacent characters. For example, for "`Mississippi`", it should return "`Misisipi`".

   c) Write a function that, given a non-negative integer n, returns a list with 1,2,2,3,3,3,4,4,4,... until n repeated n times.

   d) Write a function that, given a list of values, returns the index of the first occurrence of the highest value. You can admit that the list is not empty but you can't use the functions `max`, `find` or `index`.

###### (these exercises were created by San Jose State University Cay Horstmann)

