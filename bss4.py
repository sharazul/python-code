import urllib.request
html = input('enter link')
ur = urllib.request.urlopen(html)
for i in ur:
    print(i)
