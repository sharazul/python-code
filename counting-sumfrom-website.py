import urllib.request
from bs4 import BeautifulSoup
import re
sum = 0
url = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_1033190.html").read()
soup = BeautifulSoup(url,'html.parser')
spantag = soup('span')
for tags in spantag:
    strvalue = str(tags)
    number = re.findall('[0-9]+',strvalue)
    for j in number:
        j = int(j)
        sum = sum + j
print(sum)
