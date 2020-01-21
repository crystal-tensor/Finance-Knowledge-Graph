import re

zfc = '"董事长"  '

k=re.sub('"','',zfc)

print(k)