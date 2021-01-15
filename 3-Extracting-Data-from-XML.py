import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = urllib.request.urlopen(' http://py4e-data.dr-chuck.net/comments_1097828.xml').read()
str = link.decode()
tree = ET.fromstring(str)
lst = tree.findall('comments/comment')
print(len(lst))
z = 0
for item in lst:
    print('name : ', item.find('name').text)
    print('count : ', item.find('count').text)
    z = z + int(item.find('count').text)
print('sum : ', z)
