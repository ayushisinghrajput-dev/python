set_x = {1,2,2,3}
print(set_x)
# this is for sunbstitution method (|) and intersection method(&) 
a = {1,2,3,4}
b = {3,4,5,6}
print(a|b)
print(a&b)

# this for difference
print(a-b)
print(b-a)

# this is for power or a cap

print(a^b)
print(b^a)

print(a.issuperset(b))

print(b.issuperset(a))

a.add(6)
print(a)

a.remove(3)
print(a)

a.remove(2)
print(a)
#or discard() mein koi 

a.discard(9)
print(a)


#arbitary element uthata hai pop()

a.pop()
print(a)

# update()

a.update()
print(a)

# clear()
a.clear()
print(a)

# empty set
emp_set = set()

l = [10,10,20,20,30,40,30,20,40,50,60,70,70]
set(l)