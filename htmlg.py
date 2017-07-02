import sys
f=open('prism.html','w')
f=open('prism.html','a')
body="<body style='background-color:black'>\n"
f.write(body)
color=['darkgrey','violet','indigo','brown','lightgrey','yellow','orange','red','lightcyan','skyblue']
cpicker=0
index=0
subindx=0
notnull=[]
try:
    data=[of for of in open(sys.argv[1])]
except (IndexError):
    print ' htmlg [yourfile]'
    sys.exit()
for char in data:
    notnull.append(char)
    while notnull:
        tags="<font style='color:%s'>%s</font>"%(color[cpicker],notnull[0][subindx])
        if notnull[0][subindx] == '\n':
            f.write('<br >')
        subindx+=1
        cpicker+=1
        f.write(tags)
        if cpicker == 9:
            cpicker=0
        if len(notnull[0][0:]) == subindx:
            subindx=0
            notnull=[]
