# git add BSI.py
# added self parameter to datacenters()
import json
a = {
    "jabba" : {
        "the": "hutt"
    },
    "django" : "unchained",
    "bobba" : {
        "fett" : "the",
        "bounty" : "hunter"
    }
}
print a
for i,j in a.iteritems():
    print "-" * 5
    print i
    print j
print "*" * 5
for i in a:
    print i
print "*" * 5
print a.items()
print "*" * 5
print a.keys()
key = a.keys()[0]
print key

# json formatted printing
dictJSON = {"key": "value", "obj": {"key2": "value2"}}
print json.dumps(dictJSON, indent=4, separators=(',', ': '))
print json.dumps("SELECT instance_array_id FROM instance_arrays")
# empty array param
def fc(blabla):
    for i in blabla:
        print i
fc([])
fc([1, 2])

a = ["blabla"]
for i in a:
    print i

def func(arg = "blue"):
    print arg
func()
func("shablamey")
print "-"*5
dictA = {"blabla" : True, "chuchamanga": False, "aardvark": "fugly"}
for i, j in dictA.items():
    print i, j
print sorted(dictA.keys()).pop()
print len(dictA)

print "*"*10
s = "fname:John,lname:doe,mname:dunno,city:Florida"
sd = dict(u.split(":") for u in s.split(","))
sd2 = {}
for u in s.split(","):
    aux = (u.split(":"))
    sd2[aux[0]] = aux[1]
print sd
print sd2
s = "1, 2, 3, 4, 5"
print list(int(i)+1 for i in s.split(","))
print "a ".join(str(i) for i in range(10))
