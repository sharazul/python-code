import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x="2">
        <id>001</id>
        <name>Chuck</name>
    </user>
    <user>
        <id>009</id>
        <name>Brent</name>
    </user>
    </users>
</stuff> '''

tree = ET.fromstring(data)
lst = tree.findall('users/user')
print(len(lst))

for item in lst:
    print('id =',item.find('id').text)
    print('name = ', item.find('name').text)
    print('attribute =', item.get('x'))
