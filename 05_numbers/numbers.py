x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x)) #<class 'int'>
print(type(y)) #<class 'float'>
print(type(z)) #<class 'complex'>

a = float(x)
print(a) #1.0

b = int(y)
print(b) #2

c = complex(x)
print(c) #(1+0j)
