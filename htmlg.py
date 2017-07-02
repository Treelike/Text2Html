import os
os.system('touch file4color.txt user.txt prism.html')
f=open('prism.html','w')
f=open('prism.html','a')
body="<body style='background-color:black;font-family:lato;font-size:15px'>\n"
f.write(body)
color=['darkgrey','lightblue','pink','#988066','lightgrey','silver','#899800','cyan','lightcyan','skyblue']
file4color=[f4c.split(',') for f4c in open('file4color.txt')]
if file4color:
    if file4color[0][0:]:
        color=file4color[0][0:]
cpicker=0
index=0
subindx=0
notnull=[]
data=[of for of in open('user.txt')]
for char in data:
    notnull.append(char)
    while notnull:
        inn=notnull[0][subindx] 
        if inn == ' ':
            inn='&nbsp;'
        tags="<font style='color:%s'>%s</font>"%(color[cpicker],inn)
        if inn == '\n':
            f.write('<br >')
        subindx+=1
        cpicker+=1
        f.write(tags)
        if cpicker == len(color):
            cpicker=0
        if len(notnull[0][0:]) == subindx:
            subindx=0
            notnull=[]
