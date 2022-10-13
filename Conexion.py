_author_ : 'Topito'
_email_ : 'w595440@teco.com.ar'
USERNAME = 'w595440'
PASSWORD = 'Ytelacreistequelaibaaponer'


import re

TEXT = 'Usuario w595440 www544440 u561107 W562211 x300092 USUARIO=x300102 USER = "topo" USR = "x300106"'
rege = r'[\"\'\s\=][uwx][0-9]{6}'

salida = re.findall(rege, TEXT, re.IGNORECASE)

print(salida)
