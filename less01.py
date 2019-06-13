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
        print(" [5] - продублирую выбранный файл в текущей директории")
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
                # Необходимо выполнить проверку isfile, т.к. при попытке копирования директории будет возникать ошибка
                if os.path.isfile(file_list[i]):
                    shutil.copy(file_list[i], file_list[i] + '.dupl')
                # Чтобы цикл имел возможность завершиться нужно изменять переменную цикла        
                i += 1
        elif do == 5:
            print("Файлы в этой директории: ")
            files = os.listdir()
            print(files)
            index = int(input("Укажите индекс файла, который нужно дублировать: "))
            shutil.copy(files[index], files[index] + '.dupl')
        else:
            pass
    elif answer == 'N':
        print("До свидания!")    
    else:
        print("Неизвестный ответ")
        



