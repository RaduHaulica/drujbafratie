def fc(x):
    print x

def fc2(x):
    for i in range(x):
        fc(i)


def print_integers(values):
    def is_integer(value):
        try:
            return value == int(value)
        except:
            return False
    for v in values:
        if is_integer(v):
            print v
print_integers([1, 2, 3, "4", "gigi", 2.2])
# bla bla bla
def print_call(fn):
    def fn_wrap(*args, **kwargs): #takes any arguments
        print "Calling %s" % fn.func_name
        return fn(*args, **kwargs) # pass any arguments to fn
    return fn_wrap
cicalaca = print_call(fc2)
cicalaca(3)

# incrementor
def make_incrementor(x):
    return lambda n: n + x

f = make_incrementor(6)
print f(0)
print f(1)
print f(0)
print f(666)

