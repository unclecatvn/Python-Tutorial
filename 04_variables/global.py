# x = "awesome"

# def myfunc():
# #   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x) #Python is fantastic

# myfunc()

# print("Python is " + x) #Python is awesome

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #Python is fantastic