lines = [line.rstrip('\n') for line in open('input.txt')]

# Step G must be finished before step N can begin.

for l in lines:
    f = l.split(" ")[1]
    s = l.split(" ")[7]
    print(f + " " + s)
