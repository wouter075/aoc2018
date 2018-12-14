lines = [line.rstrip('\n') for line in open('input.txt')]

m = 1000
fabric = [[0 for i in range(m)] for j in range(m)]
s = 0

for l in lines:
    loc = l.split(" @ ")[1].split(": ")[0]
    size = l.split(" @ ")[1].split(": ")[1]
    lx = int(loc.split(",")[0])
    ly = int(loc.split(",")[1])

    sx = int(size.split("x")[0])
    sy = int(size.split("x")[1])

    for x in range(lx, lx+sx):
        for y in range(ly, ly+sy):
            fabric[x][y] += 1

f = open("output.txt", "a")
for x in range(m):
    w = ""
    for y in range(m):
        i = fabric[x][y]
        w += str(i)
        if i >= 2:
            s += 1

    f.write(w + "\n")

# part 1
print(s)
