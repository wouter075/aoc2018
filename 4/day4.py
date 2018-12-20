from operator import itemgetter

lines = [line.rstrip('\n') for line in open('input.txt')]

unsorted = []
for l in lines:
    t = l.split("] ")[0][1:]
    d = l.split("] ")[1]
    unsorted.append(
        {'time': t,
         'action': d
         }
    )
newlist = sorted(unsorted, key=itemgetter('time'))

# print(newlist)
f = open("output.txt", "a")
for x in newlist:
    w = x['time'] + ";" + x['action']
    f.write(w + "\n")

guard = 0
g = 0

times = [{'sleep': 0, 'guard': 0} for i in range(4000)]
# times = [0 for i in range(4000)]
# print(times)

# first id
tg = newlist[0]['action'].split("#")[1].split(" ")[0]

c = 0

for n in newlist:
    if "#" in n['action']:
        g = int(n['action'].split("#")[1].split(" ")[0])

    if "falls" in n['action']:
        start = int(newlist[c]['time'].split(":")[1])
        stop = int(newlist[c + 1]['time'].split(":")[1])
        diff = stop - start
        # print("[%s] - %s" % (g, diff))
        times[g]['sleep'] += diff
        times[g]['guard'] = g

    c += 1

# print(times)
maxt = 0
maxid = 0
id = 0
for t in times:
    if t['sleep'] > maxt:
        maxt = t['sleep']
        maxid = t['guard']
        # print(t)

p = False


hour = [0 for i in range(59)]
s1 = 0
s2 = 0

for n in newlist:
    if str(maxid) in n['action']:
        p = True
    if p:
        # print(n)
        if "wakes" in n['action']:
            s1 = int(n['time'][-2:])
            # print(s1)
        if "falls" in n['action']:
            s2 = int(n['time'][-2:])
            # print(s2)

    if s1 > 0 and s2 > 0:
        # print("from: " + str(s1) + " to " + str(s2))
        for s in range(s2, s1):
            hour[s] += 1

    if "wakes" in n['action']:
        p = False
        s1 = 0
        s2 = 0

start = 0
minute = 0

for m in hour:
    if max(hour) == m:
        # print("[" + str(start) + "] " + str(m))
        minute = start
    start += 1

print(maxid * minute)
