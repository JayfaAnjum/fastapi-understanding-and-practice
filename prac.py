#DICTIONARY HANDLING
# there is no order in dictionary it is unordered map
map = {1:"one",2:"two",3:"three"}

print(map)
print(type(map))

for key,value in map.items():
    print(map[key])

#getting value from key
print(map.get(1))

#getting  length of dictionary
print(len(map))


#printing all keys
print(map.keys())

#printing all values
print(map.values())

#insert
map[4] ="four"
map[1] ="one new"

print(map.items())

#remove
map.pop(1)
print(map.items())

