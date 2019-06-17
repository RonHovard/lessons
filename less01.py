# coding : utf-8

# подключаем модули
import os
import shutil
import sys

import psutil    # стороний модуль

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
        print(" [5] - продублирую указанный файл")
        print(" [6] - удалю дубликаты")
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
            print("Продублировал файлы в текущей директории")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                # Необходимо выполнить проверку isfile, т.к. при попытке копирования директории будет возникать ошибка
                if os.path.isfile(file_list[i]):
                    shutil.copy(file_list[i], file_list[i] + '.dupl')
                # Чтобы цикл имел возможность завершиться нужно изменять переменную цикла        
                i += 1
        elif do == 5:
            print("Дублированние указанного файла ")
            filename = input("Укажите имя файла: ")
            if os.path.isfile(filename):
                newfile = filename + '.dupl'
                shutil.copy(filename, newfile)
        elif do == 6:
            print("Удаление дубликатов в директории ")
            dirname = input("Укажите имя директории: ")
            file_list = os.listdir(dirname)
            i = 0
            while i < len(file_list):
                fullname = os.path.join(dirname, file_list[i])
                if fullname.endswith('.dupl'):
                    os.remove(fullname)
                i += 1    
                            
        else:
            pass
    elif answer == 'N':
        print("До свидания!")    
    else:
        print("Неизвестный ответ")
        


                                                                                
