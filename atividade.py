import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
size = int(input('Qual o tamanho de sua senha?'))
password = ''
for i in range(size):
    password += random.choice(characters)
print(password)