## Class01 - RESOLVED



#### Exercise 1 - In interactive mode, write an expression that calculates how many seconds a full day has

```python
>>> 60 * 60 * 24
86400
```



#### Exercise 2 - In interactive mode, determine the value and data type (int, float, str, ...) of each of the following expressions

```python
>>> type(1 + 2 * 5)
<class 'int'>
>>> 1 + 2 * 5
11
>>> type(num / 3.0)
<class 'float'>
>>> num / 3.0
5.666666666666667
>>> type(num / 3)
<class 'float'>
>>> num / 3
5.666666666666667
>>> type(num // 3)
<class 'int'>
>>> num // 3
5
>>> type(num % 3)
<class 'int'>
>>> num % 3
2
>>> type(volume / 0.75)
<class 'float'>
>>> volume / 0.75
13.333333333333334
>>> type(volume // 0.75)
<class 'float'>
>>> volume // 0.75
13.0
>>> type(word + 'rus')
<class 'str'>
>>> word + 'rus'
'bangrus'
>>> type(word + 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> word + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> type(word * 2)
<class 'str'>
>>> word * 2
'bangbang'
>>> 
```



#### Exercise 3 - While running 10 miles in 43 minutes and 30 seconds, which is the  average time by km? Which is the average velocity in km/h? (1 mile =  1,61 km)

```python
>>> seconds_ran = (43 * 60) + 30	# calculating how many seconds it takes to run 10miles
>>> average_seconds = seconds_ran / 16.1	# calculating how many seconds it takes to run 1km
>>> average_minutes = average_seconds / 60	# converting to minutes
>>> average_minutes	# answer to question 1
2.701863354037267	
>>> kmph = 60 / average_minutes	# dividing 1h by the average minutes of running 1km
>>> kmph	# answer to question 2 
22.206896551724142
```



#### Exercise 4 - Compute your application grade to Universidade de Aveiro in  interactive mode

```python
# please notice these grades are just for the purpose of the exercise - not the real ones!
>>> biology12_grade = 18 
>>> informatics12_grade = 20
>>> portuguese_grade = 17
>>> philosophy_grade = 16
>>> english_grade = 20
>>> mathematics_grade = 15
>>> mathematics_exam = 12
>>> biology_grade = 13
>>> physics_grade = 14
>>> final_grade = portuguese_grade + philosophy_grade + english_grade + (mathematics_grade * 0.7 + mathematics_exam * 0.3) + biology_grade + physics_grade + biology12_grade + informatics12_grade
>>> final_grade = final_grade / 8
>>> final_grade
16.5125
```