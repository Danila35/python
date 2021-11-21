import locale
import subprocess

# 1 задание:
wd1u = u'разработка'
print(wd1u)
print(type(wd1u))
wd1 = 'разработка'
print(wd1)
print(type(wd1))

wd2u = u'сокет'
print(wd2u)
print(type(wd2u))
wd2 = 'сокет'
print(wd2)
print(type(wd2))

wd3u = u'декоратор'
print(wd3u)
print(type(wd3u))
wd3 = 'декоратор'
print(wd3)
print(type(wd3))

print("-----------------")
# 2 задание:

wd1 = 'class'
wd2 = 'function'
wd3 = 'method'
wd1b = bytes(wd1, 'utf-8')
wd2b = bytes(wd2, 'utf-8')
wd3b = bytes(wd3, 'utf-8')
print(wd1b, wd2b, wd3b)
print(type(wd1b), type(wd2b), type(wd3b))
print(len(wd1b), len(wd2b), len(wd3b))

print("-----------------")
# 3 Задание:
# кирилицу нельзя перевести в байты без encode, выдаст ошибку

wd1 = b"attribute"
wd2 = "класс".encode('utf-8')
wd3 = "функция".encode('utf-8')
wd4 = b"type"

print(wd1, wd2, wd3, wd4)
print("-----------------")
# 4 задание:

wd1 = u'разработка'
print(wd1.encode('utf-8').decode('utf-8'))
wd2 = u'администрирование'
print(wd2.encode('utf-8').decode('utf-8'))
wd3 = u'protocol'
print(wd3.encode('utf-8').decode('utf-8'))
wd4 = u'standard'
print(wd4.encode('utf-8').decode('utf-8'))

print("-----------------")
# 5 задание:

args = ['ping', 'yandex.ru']
subproc_ping_ya = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping_ya.stdout:
    print(line.decode('cp866').encode('utf-8').decode('utf-8'))

args_yt = ['ping', 'youtube.com']
subproc_ping_yt = subprocess.Popen(args_yt, stdout=subprocess.PIPE)
for line in subproc_ping_yt.stdout:
    print(line.decode('cp866').encode('utf-8').decode('utf-8'))

# 6 задание:
# кодировкуа файла по умолчанию
print(locale.getpreferredencoding())
file = open("test_file.txt", "w")
file.write("сетевое программирование\n")
file.write("сокет\n")
file.write("декоратор\n")
print(file.encoding)
file.close()

with open("test_file.txt", encoding='utf-8') as file:
    for line in file:
        print(line, end='')
