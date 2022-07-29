from cryptography.fernet import Fernet
from datetime import datetime, timedelta
import math
import time

# Generamos una clave
key = Fernet.generate_key()
#key = b'WbONkjzh48sO347wQna_R-KcDmSBAuphkLsj7FnFs4M='

print("Key: ", key)

# Creamos la instancia de Fernet
# Parametros: key: clave generada

f = Fernet(key)

# Encriptamos el mensaje
# utilizando el método "encrypt"
token = f.encrypt(b'casa de la vaca')

# Mostramos el token del mensaje
print("Token: ", str(token, 'utf-8'))

interval = 30
current_time = datetime.now() + timedelta(seconds=3)
unixtime = (time.mktime(current_time.timetuple()))
time_rounded = math.floor(unixtime)

print("Unix time: ", time_rounded)

window = 60
epoch = datetime.fromtimestamp(0)
print(epoch)
timenow = datetime.now()
print(timenow)

#timekey = math.floor(20000000000 / window)
timekey = math.floor((timenow - epoch).total_seconds() / window)

print("TOTP Time: ", timekey)
