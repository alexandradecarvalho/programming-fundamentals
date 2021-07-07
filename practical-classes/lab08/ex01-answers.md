## Lab08 Ex. 1 - RESOLVED



#### Exercise 1 - Try to predict the result and effects of each of the instructions below - some of them don't have a result and others throw errors

```python
shop = {'eggs':6, 'sugar':1.0}
shop							# {'eggs':6, 'sugar':1.0}
{'sugar':1,'eggs':6} == shop	# True? The 1 should cast to double and dictionaries are unordered 
type(shop)						# dict
len(shop)						# 2 
shop[0]							# ERROR - 0 is not a key of shop
shop['eggs']					# 6
'eggs' in shop					# True
6 in shop						# False - Only considering keys...
shop[6]							# ERROR - 0 is not a key of shop
shop.get(6)						# Doesn't throw error but doesn't return anything either
shop['sugar'] = 2.0				 
shop							# {'eggs':6, 'sugar':2.0}
shop.append('beer')				# ERROR - can't append to a dictionary!
shop['beer'] = 6*0.33			
shop							# {'eggs':6, 'sugar':2.0, 'beer':1.98}
len(shop)						# 3
shop['beer'] += 0.33
shop							# {'eggs':6, 'sugar':2.0, 'beer':2.31}
shop.keys()						# dict_keys(['eggs','sugar','beer'])
shop.items()					# dict_items([('eggs',6), ('sugar',2.0), ('beer',2.31)])

d = {}
type(d); len(d); d				# dict \n 0 \n {}
d[93542] = {'maria', 'P1'}
d[95612] = {'daniel', 'P2'}
d[76367] = {'john', 'P1'}
len(d); d						# 3 \n {93542:{'maria', 'P1'}, 95612: {'daniel', 'P2'}, 76367: {'john', 'P1'}}
d[95612][1]
for x in d:
    print(x,d[x])				# 93542 {'maria', 'P1'} \n 95612 {'daniel', 'P2'} \n 76367 {'john', 'P1'}
for x,y in d.items():
    print(x,y,sep='->')			# 93542->{'maria', 'P1'} \n 95612->{'daniel', 'P2'} \n 76367->{'john', 'P1'}
t = {'P1':[], 'P2':[]}
for x in d:
    t[d[x][1]].append(d[x][0])	# ERROR - d[x] is a set, so d[x][1] is invalid because sets aren't ordered
len(t['P1'])					# 0
t	# compare results!
t.pop('P2')						# []
t								# {'P1':[]}
```

