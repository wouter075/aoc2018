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

times = [{'sleep': 0, 'guard': 0,
          '0': 0,
          '1': 0,
          '2': 0,
          '3': 0,
          '4': 0,
          '5': 0,
          '6': 0,
          '7': 0,
          '8': 0,
          '9': 0,
          '10': 0,
          '11': 0,
          '12': 0,
          '13': 0,
          '14': 0,
          '15': 0,
          '16': 0,
          '17': 0,
          '18': 0,
          '19': 0,
          '20': 0,
          '21': 0,
          '22': 0,
          '23': 0,
          '24': 0,
          '25': 0,
          '26': 0,
          '27': 0,
          '28': 0,
          '29': 0,
          '30': 0,
          '31': 0,
          '32': 0,
          '33': 0,
          '34': 0,
          '35': 0,
          '36': 0,
          '37': 0,
          '38': 0,
          '39': 0,
          '40': 0,
          '41': 0,
          '42': 0,
          '43': 0,
          '44': 0,
          '45': 0,
          '46': 0,
          '47': 0,
          '48': 0,
          '49': 0,
          '50': 0,
          '51': 0,
          '52': 0,
          '53': 0,
          '54': 0,
          '55': 0,
          '56': 0,
          '57': 0,
          '58': 0,
          '59': 0,

          } for i in range(4000)]
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

        # part 2
        for x in range(start, stop):
            times[g][str(x)] += 1

    c += 1

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

maxg = 0
maxmin = 0

for x in times:
    if x['guard'] > 0:
        for i in range(0, 59):
            if int(x[str(i)]) > maxmin:
                maxmin = int(x[str(i)])
                maxg = x['guard']

print(maxmin * maxg)
#  18943 to low

