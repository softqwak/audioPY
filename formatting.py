import re

def formatting(command, activity = None, typeobj = None):
    # command = re.sub(" ", "_", command)

    # TODO
    # Нужно добавить условный оператор на переменную активити
    # чтобы при разных вариантах формулировки задачи
    # отформатированный текст нёс в себе один смысл
    # 
     
    command = re.sub(" точка", "", command)
    command = re.sub("tvxt|txt|tx3", ".txt", command)
    command = re.sub(" doc| дог| док", ".doc", command)
    command = re.sub(".docумент", " документ", command)
    command = re.sub("_mp3", "_.mp3", command)
    command = re.sub("в папки| папки", "в папке", command)
    
    if typeobj is not None:
        command = re.sub(" pdf", ".pdf", command)
        command = re.sub("файл.pdf", "файл pdf", command)
    

    if activity is not None and typeobj is not None:
        command = re.sub(activity+" ", "", command)
        command = re.sub(typeobj+" ", "", command)

    return command
