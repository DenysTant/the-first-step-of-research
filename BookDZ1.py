#...!
'''Задача 1
Создайте собственную программу «Адресная книга», 
работающую из командной строки и позволяющую просматривать, 
добавлять, изменять, удалять или искать контактные
данные ваших знакомых. Кроме того, эта информация также 
должна сохраняться на диске для последующего доступа.
Задача 2
Реализуйте команду replace. Эта команда заменяет одну 
строку другой в списке переданных ей файлов.'''

import os, sys, pickle

ContList = []

def FunP1_tryOpenFile(varPathFile, storedlist = []):
    if os.path.isfile(varPathFile):
        None
    else:
        print('Unable to find ',varPathFile,' file')
        print('Free-fill file will be created')
        with open(varPathFile, "ab") as varWordsFile:
            pickle.dump(storedlist, varWordsFile)
    return varPathFile #storedlist

def FunCorrector1(var_answer0 = None):
    try:
        var_answer0 = int(input())
    except ValueError:
        print("incorrectly input\nPlease try again (or 0 for exit):")
        var_answer0 = FunCorrector1(var_answer0)
    return var_answer0

def FunViewer():
    ContList = FunCOpener()[0]
    for i in ContList:
        print(i)

    FunMyMenu()###### time to change
    return 3

def FunCreator(var_nsw: list):
    print("You must input Name, and Phone\n")
    Name = input("Enter the Name: ")#add try!
    phone = input("Enter the phone: ")#add try!
    ni = {}
    ni.update({Name:phone})
    ContList.append(ni)

    with open(var_nsw[1], "wb") as varWordsFile:
        pickle.dump(ContList, varWordsFile)

    return 1

def FunCOpener():
    MContactList = FunP1_tryOpenFile('ABook.txt')
    f = open(MContactList, 'rb')
    storedlist = pickle.load(f) # загружаем объект из файла
    return [storedlist, 'ABook.txt'] #MContactList

def FunCensor(var_nsw = 3, var_type = 0):
    while var_nsw != 0:
        if var_type == 0:
            if var_nsw == 1:
                var_nsw = FunViewer()
            elif var_nsw == 2:
                var_nsw = FunCreator(FunCOpener())
            else:
                print("incorrectly input\nPlease try again (or 0 for exit):")
                var_nsw = FunCensor(FunCorrector1(var_nsw))
    else:
        sys.exit()

def FunMyMenu():
    print("Menu:\n1) Find info\n2) Addition new contact\n0) Exit\n")
    var_answer0 = FunCorrector1()
    FunCensor(var_answer0)

def FuncInit1():
    print("Hello! Welcome to simple program address-book\n \
        Set your choice what to do:")
    FunMyMenu()

def main():
    FuncInit1()

if __name__ == "__main__":
    main()
