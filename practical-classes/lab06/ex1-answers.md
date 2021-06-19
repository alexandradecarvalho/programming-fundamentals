## Lab 06 - RESOLVED



#### Exercise 1 - Try to guess the result of each of the following instructions. Some of them don't have a result and others throw errors. Use Python in interactive mode to confirm.

```python
>>> lst = [5,3,8,7]
>>> len(lst)	# Predicted result: 4; Real result: 4
>>> lst[2]		# Predicted result: 8; Real result: 8
>>> lst[4]		# Predicted result: IndexOutOfBoundError (or is this Java?); Real result: IndexError (more like Python ;) )
>>> lst[-4]		# Predicted result: 5; Real result: 5
>>> lst[1:3]	# Predicted result: [3,8]; Real result: [3,8]
>>> lst[:-1]	# Predicted result: [5,3,8]; Real result: [5,3,8]
>>> lst[2:2]	# Predicted result: []; Real result: []
>>> lst[2:2] = [99]
>>> lst 		# Predicted result: [5,3,99,8,7]; Real result: [5,3,99,8,7]
>>> lst.append(33)
>>> lst 		# Predicted result: [5,3,99,8,7,33]; Real result: [5,3,99,8,7,33]
```

#### 