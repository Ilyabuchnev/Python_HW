
# Задача 2

a = int(input('Введите значение врмени в секундах '))
b = a//3600
c = int(((a/3600)-(a//3600))*60)
d = a - ((b*3600) + ( c*60))
print(str(b) + ":" + "%02d" % c + ":" + "%02d" % d)