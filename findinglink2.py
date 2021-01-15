import urllib.request
from bs4 import BeautifulSoup
import re

inputurl = input('Enter url: ')
position  = int(input('Enter position '))
count = int(input('Enter count '))
url = urllib.request.urlopen(inputurl).read()
while count >= 1:
    soup = BeautifulSoup(url,'html.parser')
    links = soup('a')
    sum = 1
    for link in links:
        if sum == position:
            link = str(link)
            relink = re.findall('http:.+.html',link)
            url = urllib.request.urlopen(relink[0])
        if sum > position:
            break
        else:
            sum = sum + 1
    count = count - 1
    print(relink)
