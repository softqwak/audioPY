import json
import sys
import os
from pprint import pprint # временно
import easygui
from settingDirectiorys import settingDirectorys

#
# import subprocess

class main():
    
    def __init__(self):
        super().__init__()
        with open("data\commands.json", "r", encoding="utf-8") as read_file:
            self.commands = json.load(read_file)
        with open("data\profile.json", "r", encoding="utf-8") as read_file:
            self.profile = json.load(read_file)
        with open("data\settings.json", "r", encoding="utf-8") as read_file:
            self.settings = json.load(read_file)

        if (self.profile["login"] == ""):
            if(self.__registration()):
                pass
            else:
                print("Ошибка регистрации")
        else:
            if (self.__signin()):
                # Использовать мудоль subprocess
                print("Вы вошли в программу")
                os.system("python audioget.py " + self.settings["name"])

    def __wrset(self):
        with open('data\settings.json', 'w', encoding="utf-8") as outfile:
            json.dump(self.settings, outfile)
    def __wrprof(self):
        with open('data\profile.json', 'w', encoding="utf-8") as outfile:
            json.dump(self.profile, outfile)
    def __wrcom(self):
        with open('data\commands.json', 'w', encoding="utf-8") as outfile:
            json.dump(self.commands, outfile)

    def __registration(self):
        self.settings["paths"].extend((
            str((os.getcwd())[0]) + ":/Users/" + os.getlogin() + "/Desktop", 
            str((os.getcwd())[0]) + ":/Users/" + os.getlogin() + "/Downloads", 
            str((os.getcwd())[0]) + ":/Users/" + os.getlogin() + "/Documents",
            str((os.getcwd())[0]) + ":/Programm Files",
            str((os.getcwd())[0]) + ":/Programm Files (x86)")
        )
        print("""
            Вас приветсвует программа \"ГОЛОСОВОЙ ПОМОЩНИК\"
            Для начала давайте создадим ваш профиль!
            """.upper())
        log=str(input("Введите ваш  логин: "))
        if(log != ""): self.profile["login"]  = log
        else: return False
        pas  = str(input("Введите ваш пароль: "))
        if (pas != ""): self.profile["password"] = pas
        else: return False

        print("""
            Отлично! Не забудте ваши даннные, они еще потребуются.
            """.upper())

        print("""
            Теперь Вам нужно выбрать имя ваше будущему голосовому 
            помощнику спомощью которого вы сможете обращаться 
            к нему для выполнения задач
            """.upper())
        
        self.settings["name"] = str(input("Введите имя Вашего голосового помощника: "))
        print("""
            Чтобы программа смогла выполнить вашу команду необходимо, 
            чтобы в предложении было озвученно имя - """.upper() + self.settings["name"].upper())
        
        print("""
            Здесь должен быть список функций
            -
            -
            -
            -
            
            Тут проверка микрофона и обучение
            -
            -
            -

            Результаты качества микрафона для использования программы
            """.upper())

        print("""
            Для продолжения Вам необходимо выбрать директории по которым 
            голосовой помошник будет искать требуемые файлы и папки 
            чем больше и конкретнее пути к директориям будут выбраны, 
            тем более быстрее и качественнее программа будет 
            выполнять команды пользователя!

            Если Вы еще не знаете какие директории выбрать, то
            можете просто пропустить этот этап и пользоваться
            уже заранее определёнными директориями
            
            Настоятельно рекомендуем выбрать часто используемые папки, 
            папки в разделе быстрый доступ проводника и папки, в которых
            вы храните наибольшее количество документов по работе или учёбе
            Например:
            -{}
            -{}
            -{}
            -{}
            """.format("C:/Users/" + os.getlogin() + "/Desktop", 
            "C:/Users/" + os.getlogin() + "/Downloads", 
            "C:/Users/" + os.getlogin() + "/Documents", 
            "C:/Users/" + os.getlogin() + "/...").upper())

        ans = "1"
        paths = []
        while ans == "1":
            ans = str(input("Добавить директорию Да/Нет? (1/0): "))
            if ans == "1":
                paths.append(easygui.diropenbox())

        ans=0
        if paths != []:
            paths = settingDirectorys(paths)
            self.settings["paths"].extend(paths)
        
        del paths, ans, log, pas
        self.__wrprof()
        self.__wrset()

        print("Запустите заново программу и пройдите авторизацию")
        return True

    def __signin(self):
        print("""
            Вас приветсвует программа \"ГОЛОСОВОЙ ПОМОЩНИК\"
            Пройдите авторизацию в Ваш профиль!
            """)

        while True:
            log  = str(input("Введите ваш  логин: "))
            if (log == ""): return False
            pas  = str(input("Введите ваш пароль: "))
            if (pas == ""): return False

            if (log == self.profile["login"] and pas == self.profile["password"]): return True
            else: print("Неверный логин или пароль!"); self.__signin()

if __name__ == "__main__":
    main()