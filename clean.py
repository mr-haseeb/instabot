f = open('fitness_hastags','r')
a = ['#']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('fitness_hastags_clean','w')
for line in lst:
    f.write(line)
f.close()