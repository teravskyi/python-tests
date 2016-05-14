# init variables
mystring = "somestring"
myfloat = 10.0
myint = 20

# testing code
if mystring == "somestring":
    print ("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print ("Float: %d" % myfloat)
if isinstance(myint, int) and myint == 20:
    print ("Integer: %d" % myint)