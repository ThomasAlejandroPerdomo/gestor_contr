import random
con_dig = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lon_p = int(input("Ingresa la longitud de la contraseña: "))

elem_p = ""
for i in range(lon_p):
    elem_p += random.choice(con_dig)
print("tu contraseña es: ",elem_p)



