poly = open("input.txt").read()

for y in range(2000):
    for x in range(len(poly)):
        if x > 0:
            comp = poly[x:x+2]
            if len(comp) == 2:
                if comp[0] != comp[1]:
                    if comp[0].upper() == comp[1].upper():
                        poly = poly.replace(comp, "")
                        print("match!" + comp + str(len(poly)))

