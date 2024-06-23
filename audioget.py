import os
from sys import argv
import subprocess
import speech_recognition as sr
import re

class audioget():
    text_command = ""
    def __init__(self):
        super().__init__()
        self.__run()

    def __run(self):
        while True:
            self.text_command = self.__command()
            if argv[1] in self.text_command:
                self.text_command = re.sub(" "  + 
                argv[1] + "|" + argv[1] + " ", "", self.text_command)
                os.system("python analysis.py " + "\"" + self.text_command + "\"")
            # process = subprocess.Popen(["analysis.py", self.text_command], stdout=subprocess.PIPE)
            
    def __command(self):
        try:
            self.record = sr.Recognizer()
            with sr.Microphone() as source:
                print("Говори")
                self.record.pause_threshold = 0.7
                self.record.adjust_for_ambient_noise(source, duration=1)
                voice = self.record.listen(source)
        except OSError:
            print("Внутренняя ошибка: проверьте подключение микрофона, программа не может получить доступ к микрофону!")
            os.system("TASKKILL /F /IM python.exe /T")
        try:
            text = self.record.recognize_google(voice, language='ru-RU').lower()
        except sr.UnknownValueError:
            print('...')
            text = self.__command()

        return text

if __name__ == "__main__":
    audioget()