import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
size = int(input('Qual o tamanho de sua senha?'))
password = ''
amount = int(input('Quantas senhas você quer criar?'))
for i in range(amount):
    for j in range(size):
        password += random.choice(characters)
print(password)