# coding : utf-8

import os
import psutil    # стороний модуль
import sys

# Комментарий

print("НАЧАЛО ПУТИ!")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = input("Давай поработаем? (Y/N)")

# PEP-8 Рекомендации по оформлению кода (документ)

if answer == 'Y':
    print("Отлично,", name,"!")
    print("Я умею:")
    print(" [1] - выведу список файлов текущей директории")
    print(" [2] - выведу информацию о системе")
    print(" [3] - выведу список процессов")
    do = int(input("Укажите номер действия: "))
    
    if do == 1:
        print(os.listdir())
    elif do == 2:
        print("Имя текущей директории:", os.getcwd())
        print("Платформа ОС:", sys.platform)
        print("Кодировка файловой системы:", sys.getfilesystemencoding())
        print("Логин пользователя системы:", os.getlogin())
        print("Количество CPU:", psutil.cpu_count())
    elif do == 3:
        print(psutil.pids())
    else:
        pass
elif answer == 'N':
    print("До свидания!")    
else:
    print("Неизвестный ответ")
    
