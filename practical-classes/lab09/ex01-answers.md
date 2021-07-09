## Lab09 Ex. 1 - RESOLVED



#### Exercise 1 - Using Python in interactive mode, execute the instructions below and interpret the results. Try to predict the results of each expression

```python
lx = [1,3,5,7,9]
[10+x for x in lx]						# [11,13,15,17,19]
ly = [2,4,6]
[x+y for x in lx for y in ly]			# [3,5,7,5,7,9,7,9,11,9,11,13,11,13,15]
{x+y for x in lx for y in ly}			# {3,5,7,9,11,13,15}
[(x,y) for x in lx for y in ly]			# [(1,2),(1,4),(1,6),(3,2),(3,4),(3,6),(5,2),(5,4),(5,6),(7,2),(7,4),(7,6),(9,2),(9,4),(9,6)]
[(x,y) for y in ly for x in lx]			# [(1,2),(3,2),(5,2),(7,2),(9,2),(1,4),(3,4),(5,4),(7,4),(9,4),(1,6),(3,6),(5,6),(7,6),(9,6)]
[x*c for c in "abc" for x in lx]		# ['a','aaa','aaaaa','aaaaaaa','aaaaaaaaa', 'b','bbb','bbbbb','bbbbbbb','bbbbbbbbb','c','ccc','ccccc','ccccccc','ccccccccc']
[x%3==0 for x in lx]					# [False,True,False,False,True]
[(x,x//3) for x in lx if x%3==0]		# [(3,1),(9,3)]
{x:x//3 for x in lx if x%3==0}			# {3:1, 9:3}
[(x,y) for x in lx for y in ly if x<y]	# [(1,2),(1,4),(1,6),(3,4),(3,6),(5,6)]
{x:[y for y in ly if x<y] for x in lx}	# {1:[2,4,6], 3:[4,6], 5:[6], 7:[], 9:[]}
any(x%2==0 for x in lx)					# False
```

