from collections import Counter

lines = [line.rstrip('\n') for line in open('input.txt')]
two = 0
three = 0

# part #1
for l in lines:
    c = Counter(l)
    for i in c.items():
        if i.count(2) > 0:
            two += 1
            break
    for i in c.items():
        if i.count(3) > 0:
            three += 1
            break
# part 1
print(two * three)

# part 2
two = 0
three = 0
for l1 in lines:
    for l2 in lines:
        if l1 != l2:
            # print(l)
            # print(k)
            # print("-"*30)
            if (len([i for i in range(len(l1)) if l1[i] != l2[i]])) == 1:
                print(l1)
                print(l2)
