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

guard = 0
g = 0
start = ""
stop = ""
times = [{'sleep': 0, 'guard': 0} for i in range(4000)]
# print(times)

for n in newlist:
    if "#" in n['action']:
        g = n['action'].split("#")[1].split(" ")[0]
        start = ""
        stop = ""

    if g != guard:
        a = n['action'].split(" ")[0]
        # print(a)
        if a == "falls":
            start = n["time"]
        if a == "wakes":
            stop = n["time"]

        if start != "" and stop != "":
            s1 = int(start.split(":")[1])
            s2 = int(stop.split(":")[1])
            sleep = s2 - s1
            # print(str(sleep) + " - " + str(g))
            times[int(g)]['sleep'] += sleep
            times[int(g)]['guard'] = g

            guard = g

maxt = 0
maxid = 0
id = 0
for t in times:
    if t['sleep'] > maxt:
        maxt = t['sleep']
        maxid = t['guard']

for n in newlist:
    if maxid in n['action']:
        print(n)

# nope, not yet :P
