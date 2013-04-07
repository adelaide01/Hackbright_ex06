from sys import argv
script, txt = argv

f = open(txt)
twain = f.read()

#print twain


#creates a dict called count  
count = {}

for line in twain.split():
    if line in count:
        count[line] += 1
    else:
        count[line] = 1

for line in count:
    print line, count[line]
    