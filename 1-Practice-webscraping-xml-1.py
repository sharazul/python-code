import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl"> +1 734 303 4456 </phone>
    <email hide="yes" />
 </person> '''

tree = ET.fromstring(data)  # convert string into xml tree
lst = tree.find('name').text # now we can use operation on xml tree
print(lst)
