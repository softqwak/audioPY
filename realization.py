import os
import json
from sys import argv
import subprocess
# from pprint import pprint

class realization():

    def __init__(self):
        super().__init__()
        with open("data\settings.json", "r", encoding="utf-8") as read_file:
            self.settings = json.load(read_file)
        self.file = "" 
        self.path = ""
        self.shell_process = ""
        self.__run()
    

    def __run(self):
        """
        argv[1] - действие
        argv[2] - объект над которым совершается действие
        argv[3] - наименование объекта, если такое имеется
        argv[4, 5, 6, ..] - короткий путь к объекту  """

        successful = False
        package = ""

        for i in range(4, len(argv)): package += "/"+argv[i]

        if (argv[2] == "файл" or "документ" or "презентацию" or "таблицу" or "файл pdf" or "папку"):
            for path in self.settings["paths"]:
                path += package
                print(path)
                for file in os.listdir(path):
                    try:
                        print(file)
                        if (file.split('.')[0] == argv[3]):
                            self.path = path
                            self.file = file
                            successful = True
                            break
                    except:
                        print()        
                if successful:
                    break

            if argv[1] == "открой":
                self.__open()            
            elif argv[1] == "закрой":
                self.__close()
            elif argv[1] == "удали":
                self.__delet()
            elif argv[1] == "создай":
                self.__creat()
            if argv[1] == "отмени действие":
                # TASKKILL /IM winword.exe
                pass
    
    def __open(self):
        print("Открываю {} в папке {}".format(argv[3], self.path))
        if argv[2] == "папку":
            os.system("start " + os.path.join(self.path, self.file))
        else:
            self.shell_process = subprocess.Popen([os.path.join(self.path, self.file)],shell=True) 
        
    def __close(self):
##        parent = psutil.Process(self.shell_process.pid)
##        children = parent.children(recursive=True)
##        child_pid = children[0].pid
##        subprocess.check_output("Taskkill /PID %d /F" % child_pid)
        pass

    def __delet(self):
        pass

    def __creat(self):
        pass
        
if __name__ == "__main__": 
    realization()
        
