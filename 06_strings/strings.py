a = "Hello, World!"
print(len(a)) #13

txt = "The best things in life are free!"
print("free" in txt) #True

txt = "The best things in life are free!"
print("expensive" in txt) #False

for x in "banana":
  print(x) #b a n a n a
  
a = "Hello, World!"
print(a[1]) #e

b = "Hello, World!"
print(b[-5:-2]) #orl

# Index dương:  H  e  l  l  o  ,     W  o  r  l  d  !
#               0  1  2  3  4  5  6  7  8  9 10 11 12

# Index âm   : -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")





