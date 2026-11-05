l1 = [10,20,30,40]
t1 = (10,20,30,40)

l2 = [1,2,3,4,5,6,7,8,9,10]

print(l2[5:])
print(l2[-4])

# list slicing
t2 = (10,30,70,60,80)
print(t2[4])


# list to print all numbers from 1-1001
l3 = [i for i in range(1,1001)]
print(l3)

# list to print the even numbers from 1-100
l4 = [i for i in range(1,100) if i%2 == 0]
print(l4)

# list to print the 0dd numbers from 101-103
l5 = [i**3 for i in range(101,130) if i%2!=0]
print(l5)

l6 = [55,67,98,200,101] 
new_l7 = [i**3 for i in l5 if i%2!=0]

(l6.append(90))
(l6.insert(40)) 
remove(67)
(l6.pop())       


# addition of two lists
a= [4,5,3,6,2]
b = [9,4,3,0,5]
print(a+b)
print(b+a)
print(a*2)


# tuple slicing
t3 = (i for i in range(1,100))
print(t3)

# 