import hashlib  # Se importa hashlib

contraseña = input("Contraseña\n")
contraseña_cifrada = hashlib.sha512(contraseña.encode())
print("Su contraseña cifrada es:")
print(contraseña_cifrada.hexdigest()) 