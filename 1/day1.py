lines = [line.rstrip('\n') for line in open('input.txt')]
start = 0
freq = []

# for x in range(200):
for l in lines:
    # part #1
    if l[0] == "+":
        start += int(l[1:])
    else:
        start -= int(l[1:])
# part 1
print(start)

# part 2
lines = [line.rstrip('\n') for line in open('input.txt')]
loop = True
start = 0
while loop:
    for l in lines:
        # part #1
        if l[0] == "+":
            start += int(l[1:])
        else:
            start -= int(l[1:])

        if start not in freq:
            freq.append(start)
        else:
            print(start)
            loop = False

