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
