import easygui

def settingDirectorys(paths):
    print("""
            Выбранные директории:
        """.upper())
    for item in paths: print("""            """ + item)
    print("""
            ------------------------""")
    ans = str(input("""
            1.ДОБАВИТЬ ДИРЕКТОРИЮ
            2.УДАЛИТЬ ДИРЕТОРИЮ
            3.ПРОДОЛЖИТЬ

Введите число: """))
    if ans == "1":
        while ans == "1":
            if ans == "1":
                paths.append(easygui.diropenbox())
            ans = str(input("Выбрать директорию Да/Нет? (1/0): "))
    if ans == "2":
        print("""
            Выбранные директории:
            """.upper())
        for item in paths: print("""            """ + item); print()
        try:
            paths.pop(int(input("Удалить директорию под номером: ")) - 1)
        except IndexError:
            print("Директории под таким номером нет.".upper())
            ans="0"
    
    if ans == "3":
        return paths
    else:
        settingDirectorys(paths)