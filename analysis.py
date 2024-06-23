import json
import os
from sys import argv
import subprocess
import re
from pprint import pprint
from formatting import formatting

class analisis():

    def __init__(self):
        super().__init__()
        self.activity = ""
        self.typeobj = ""
        self.nameobj = ""
        self.paths = []
        with open("data\commands.json", "r", encoding="utf-8") as read_file:
            self.commands = json.load(read_file)
        self.__run()
        

    def __run(self):
        argv[1] = formatting(argv[1])
        argv[1] = formatting(argv[1], typeobj=self.typeobj)

        print("Анализ [\""+ argv[1] + "\"]")
        # pprint(self.commands)


        if list(self.commands["basic"]["activity"].keys())[0] in argv[1]:
            self.activity = "выключись"
            print("выход")
            os.system("TASKKILL /F /IM python.exe /T")
        
        # Этап определения действия
        act=""
        obj=""
        for act in list(self.commands["basic"]["activity"].keys()):
            if act in argv[1]:
                self.activity = act
                for obj in list(self.commands["basic"]["activity"][act]):
                    if obj in argv[1]:
                        self.typeobj=obj
                        break
                break
        del act
        del obj
        # print("-"+self.activity)
        # print("-"+self.typeobj)
        strpath=""
        argv[1] = formatting(argv[1], activity=self.activity, typeobj=self.typeobj)
        # print(argv[1])
        try:
            self.nameobj = argv[1][:argv[1].index('в ')-1]
            strpath =  argv[1][argv[1].index("в "):]            
        except ValueError:
            self.nameobj = argv[1]
            strpath = ""

        strpath = re.sub(" в папке ", ">", strpath)
        strpath = re.sub("в папке ", "", strpath)
        b=""
        while ">" in strpath:
            b = strpath[:strpath.index('>')]
            self.paths.append(b)
            strpath = re.sub(b+">", "", strpath)
        self.paths.append(strpath)

        del strpath, b
        path = "python realization.py " + self.activity +" \"" + self.typeobj + "\" \"" + self.nameobj + "\""
        for item in self.paths:
            path += " \"" + item + "\""
        os.system(path)
        # #Этап определния объекта взаимодействия
        # if argv[1] in self.commands["basic"]["object"][0]:
        #     self.typeobj = self.commands["basic"]["object"][0][0]
            
"""
В скрипт передаётся строка(argv[1]) полученная от
скрипта audioget.py где содержится команда
для голосового помощника """

if __name__ == "__main__":
    analisis()