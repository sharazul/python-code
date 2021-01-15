import urllib.request
from bs4 import BeautifulSoup
import re
count = 3
repeat = 4
url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.htm').read()
while repeat >= 1:
    soup = BeautifulSoup(url,'html.parser')
    links = soup('a')
    sum = 1
    for link in links:
        if sum == count:
            link = str(link)
            relink = re.findall('http:.+.html',link)
            url = urllib.request.urlopen(relink[0])
        if sum > 3:
            break
        else:
            sum = sum + 1
    repeat = repeat - 1
    print(relink)
