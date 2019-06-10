# coding : utf-8

import os
import psutil    # стороний модуль
import shutil
import sys

# Комментарий

print("НАЧАЛО ПУТИ!")
print("Привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать в мир Python!")

answer = ''
# PEP-8 Рекомендации по оформлению кода (документ)
while answer != 'q':
    answer = input("Давай поработаем? (Y/N/q)")
    if answer == 'Y':
        print("Отлично,", name,"!")
        print("Я умею:")
        print(" [1] - выведу список файлов текущей директории")
        print(" [2] - выведу информацию о системе")
        print(" [3] - выведу список процессов")
        print(" [4] - продублирую файлы в текущей директории")
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
        elif do == 4:
            print("Дублирование файлов в текущей директории:")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                newfile = file_list[i] + '.dupl'
                shutil.copy(file_list[i], newfile)#копируй
                i += 1    
        else:
            pass
    elif answer == 'N':
        print("До свидания!")    
    else:
        print("Неизвестный ответ")
        



