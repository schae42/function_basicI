#1
def a():
    return 5
print(a())

#var    a
#val    5
#output 5

#2
def a():
    return 5
print(a()+a())

#var    a  
#val    10
#output 10

#3
def a():
    return 5
    return 10
print(a())

#var    a    
#val    5
#output 5

#4
def a():
    return 5
    print(10)
print(a())

#var    a
#val    5 
#output 5

#5
def a():
    print(5)
x = a()
print(x)

#var   a 
#val   5
#output 5 

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#var    b       c
#val    1,2     2,3
#output 3,5

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#var    b       c
#val    2       5
#output 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#var        b        
#val        100
#output     100,10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#var        b           c
#val        2,5,2,5     3,3,3,3
#output     7,14,21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#var        b       c
#val        3       5
#output     8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#var        b
#val        500,300
#output     500,500,300,500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#var        b
#val        500,300
#output     500,500,300,500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#var        b
#val        500,300
#output     500,500,300,300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#var        a()     b()
#val        1       2,3
#output     1,3,2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

#var        a      b        a()     b() 
#val        1       3       10      5        
#output     1,3,5,10
