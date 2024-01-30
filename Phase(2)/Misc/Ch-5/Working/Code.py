with open('/Users/sammgharish/Desktop/Pent/Phase(2)/Misc/Ch-5/Org File/Content.txt', 'r') as f:
    data = f.read()

l = []
li = ''
for i in range(0, len(data), 2):
    l.append(data[i:(i+2)])

for i in l:
    li += (chr(int(i, 16)))

print(li)