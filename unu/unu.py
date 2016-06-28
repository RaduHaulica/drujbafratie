# poate scriu ceva in python
# list
lista = "Unu doi trei patru cinci sase sapte"
things = lista.split(" ")
more_things = ["one", "two", "three", "four", "five"]

while len(things) < 10:
    next = more_things.pop()
    print "Adding :", next
    things.append(next)
    print "There are %d items in the list." % len(things)

print "Boom shakalaka :", things
print "Last item :", things[-1]
print " ".join(things)
print "#".join(things[2:5])
# dictionary
judete = {
    "Iasi": "IS",
    "Bucuresti": "B",
    "Brasov": "BV",
    "Constangeles": "CT",
    "Botosani": "BT"
}

orase = {
    "BV": "Rasnov",
    "IS": "Belcesti",
    "BT": "Flamanzi"
}

# print'em
print "-" * 10
print "Cities in BT :", orase["BT"]
print "-" * 10
print "Iasi are codul ", judete["Iasi"]
print "Orase din Brasov :", orase[judete["Brasov"]]

#toate codurile
print "_" * 10
for judet, cod in judete.items():
    print "%s are codul %s." % (judet, cod)
# toate orasele pe dupa ureche
print "_" * 10
for judet, cod in judete.items():
    oras = orase.get(cod)
    if not oras:
        print "%s are codul %s si nici un oras." % (judet, cod)
    else:
        print "%s are codul %s si orasul %s." % (judet, cod, orase[cod])

# testat daca e un judet
judet = judete.get("Timis")
if not judet:
    print "Nope, n-avem de-astea."
else:
    print "Ciubalai doamne ca e si asta."

# get with default value
oras = orase.get("TM", "Nu se este bre.")
print "Orasul din judetul TM este %s" % oras
