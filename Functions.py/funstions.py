def hello():                       #define
    print("hello world")           #define
    
hello()                            #function call
                    #hello world  (execute functoin)

def student():
    print("ram")
student()

def add(a,b):
    c=a+b
    return c
print(add(3,4))

    
def mul(x,y):
    b=x*y
    return b
print(mul(2,8))

def m2(a,b):
  return a*b


x = m2(12,2)
print("hello",x)

# write a function to print list and tuple 

t = (10,20,30,40,50)

def g_r(E):
    for i in E:
        print(i)
        
g_r(t)