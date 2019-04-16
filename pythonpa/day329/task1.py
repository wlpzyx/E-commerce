import re

pap = re.compile(r'\d*')

s = pap.search('one12twothree34four', 3, 20)
print(s)
s = pap.findall('one12twothree34four')
print(s)
s = pap.finditer('one12twothree34four')
print(s)

