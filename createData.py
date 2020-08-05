import random

path = 'data.txt'
chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'

f = open(path, "w", encoding="utf-8")

for _ in range(10):
    id = ''
    for _ in range(16):
        id = id+chars[random.randrange(35)]
    f.write(id+'\n')


f.close()