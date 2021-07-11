## Lab10 Ex. 1 - RESOLVED



#### Exercise 1 - Execute the following instructions in interactive mode and interpret the results

```python
l = ["Mario","Carla","anabela","Maria","nuno"]
sorted(l)				# (sort alphabetically by default) -> ["Carla","Maria","Mario","anabela","nuno"]
sorted(l,reverse=True)	# (the reverse as before) -> ["nuno","anabela","Mario","Maria","Carla"]
sorted(l,key=len)	# (when they have the same length, it's in entry order) -> ["nuno","Mario","Carla","Maria","anabela"]
l[0].casefold()		# "mario"
str.casefold(l[0])	# equivalent -> "mario"
sorted(l,key=str.casefold)	# (alphabetically but case insensitive) -> ["anabela","Carla","Maria","Mario","nuno"]
def lenFold(s):
    return (len(s),s.casefold())
lenFold(l[0])			#-> (5,"mario")
sorted(l,key=lenFold)	# (sorted firstly by length, then alphabetically case-insensitive) -> ["nuno","carla","maria","mario","anabela"]

d = [('Republic',1910,10,5),('Christmas',1,12,25),('Liberty',1974,4,25),('Restoration',1640,12,1)]
sorted(d)	# (alphabetically) -> [('Christmas',1,12,25),('Liberty',1974,4,25),('Republic',1910,10,5),('Restoration',1640,12,1)]
sorted(d, key=lambda t:(t[2],t[3])) # [('Liberty',1974,4,25),('Republic',1910,10,5),('Restoration',1640,12,1),('Christmas',1,12,25)]

n = [3,4,4,4,6,7,7,8]
import bisect
bisect.bisect_left(n,6)		# 4
bisect.bisect_left(n,10)	# 8
bisect.bisect_left(n,4)		# 1
bisect.bisect_right(n,4)	# 4
```

