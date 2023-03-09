#1
import os
path = os.getcwd()
dirs = os.listdir(path)
for i in dirs:
    if os.path.isdir(i):
        print(f'DIR => {i}')
    elif os.path.isfile(i):
        print(f'FILE => {i}')
#2
import os
path = input()
print(os.access(path, os.F_OK))
print(os.access(path, os.R_OK))
print(os.access(path, os.W_OK))
print(os.access(path, os.X_OK))

#3
import os
path = input() # введите путь до папки в которой находится файл
try:
    os.chdir(path)
    txt = input() # введите название файла с его расширением
    f = open(txt, 'r')
    f = f.read().split('\n')
    print(f'Количество строк: {len(f)}')
except Exception as ex:
    print(ex)

#4
filename = input()  # replace with your file name
with open(filename, "r") as file:
    cnt = 0
    for i in file:
        cnt += 1

print("The number of lines in path is: ", {cnt})

#5
items = list(map(int, input().split()))
with open('items.txt','w') as f:
	f.write('\n'.join(items))
        
#6
import string

for l in string.ascii_uppercase:
    filename = l + ".txt"
    with open(filename, "w") as file:
        print( filename)

#7
import os
path = input()
try:
    os.chdir(path)
    txt1 = input()
    path2 = input()
    txt2 = input()
    with open(txt1,'r') as n, open(path + '/' + txt2, 'a') as f:
        for line in n:
            f.write(line)
except Exception as ex:
    print(ex)

#8
import os
path = input()

try:
    os.chdir(path)
    dirs = os.listdir(os.getcwd())
    print('Выберите папку или файл для удаления: ')
    for i in dirs:
        if os.path.isdir(i):
            print(f'<DIR> {i}')
        elif os.path.isfile(i):
            print(f'<FILE> {i}')
    print('Введите имя файла:')
    name = input()
    if os.access(f'./{name}', os.W_OK):
        os.remove(name)
    else:
        print('Нет доступа к этому файлу')

except Exception as ex:
    print(ex)