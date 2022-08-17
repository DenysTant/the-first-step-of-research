# ...!
'''Задача 1
Создайте собственную программу «Адресная книга», 
работающую из командной строки и позволяющую просматривать, 
добавлять, изменять, удалять или искать контактные
данные ваших знакомых. Кроме того, эта информация также 
должна сохраняться на диске для последующего доступа.
Created at 07/2022 after reading a book "A byte of Python..." (first encounter)
'''

import os
import sys
import pickle

ContList = []


def FunP1_tryOpenFile(varPathFile, storedlist=[]):
    if os.path.isfile(varPathFile):
        None
    else:
        print('Unable to find ', varPathFile, ' file')
        print('Free-fill file will be created')
        with open(varPathFile, "ab") as varWordsFile:
            pickle.dump(storedlist, varWordsFile)
    return varPathFile  # storedlist


def FunCorrector1(var_answer0=None):
    try:
        var_answer0 = int(input())
    except ValueError:
        print("incorrectly input\nPlease try again (or 0 for exit):")
        var_answer0 = FunCorrector1(var_answer0)
    return var_answer0


def FunSubMenu1():
    print("For All list:\n1) Find info for Name\n2) Find info for Phone\n3) Delete item for Phone\n4) Change item for Phone\n5) Return to previous Menu\n0) Exit\n")
    FunCensor(FunCorrector1(), 1)


def FunViewer():
    global ContList  # ?
    ContList = FunCOpener()[0]
    for i in ContList:
        for vname, vphone in i.items():
            print(vname, '->', vphone)
    FunMyMenu()
    return 3


def FunFindForName():
    global ContList  # ?
    ContList = FunCOpener()[0]
    vFindFName = input("Enter the Name who do you find: ")
    vCountItem = 0
    if vFindFName:
        print(
            f"-----------You found {vFindFName} or not?------------------------------------\n")
        for i in ContList:
            for vname, vphone in i.items():
                if vname == vFindFName:
                    print(vname, '->', vphone)
                    vCountItem += 1
    else:
        print("Wrong input Name\n")
    if vCountItem < 1:
        print("Sorry but nothing found\n")
    FunSubMenu1()
    return 3  # 0


def FunFindForPhone():
    global ContList  # ?
    ContList = FunCOpener()[0]
    vFindFPhone = input("Enter the Phone what do you find: ")
    vCountItem = 0
    if vFindFPhone:
        print(
            f"-----------You found {vFindFPhone} or not?------------------------------------\n")
        for i in ContList:
            for vname, vphone in i.items():
                if vphone == vFindFPhone:
                    print(vname, '->', vphone)
                    vCountItem += 1
    else:
        print("Wrong input Phone\n")
    if vCountItem < 1:
        print("Sorry but nothing found\n")
    FunSubMenu1()
    return 3  # 0


def FunDelItem():
    global ContList  # ?
    ContList = FunCOpener()[0]
    vFindFPhone = input("Enter the Phone what do you Delete: ")
    vCountItem = -1
    vCountItemForDel = -1
    if vFindFPhone:
        print(
            f"-----------You want to delete recording: {vFindFPhone}  ------------------------------\n")
        for i in ContList:
            vCountItem += 1
            for vname, vphone in i.items():
                if vphone == vFindFPhone:

                    print(vname, '->', vphone, ' - is deleted now')
                    vCountItemForDel = vCountItem
                    break
            if vCountItemForDel >= 0:
                ContList.pop(vCountItemForDel)
                with open(FunCOpener()[1], "wb") as varWordsFile:
                    pickle.dump(ContList, varWordsFile)
    else:
        print("No recording to delete\n")
    if vCountItem < 1:
        print("Sorry but nothing delete\n")
    FunSubMenu1()
    return 3  # 0


def FunRewriteItem():
    global ContList  # ?
    ContList = FunCOpener()[0]
    vFindFPhone = input("Enter the Phone what do you Rewrite: ")
    vCountItem = -1
    vCountItemForDel = -1
    if vFindFPhone:
        print(
            f"-----------You want to Rewrite recording: {vFindFPhone}  ------------------------------\n")
        for i in ContList:
            vCountItem += 1
            for vname, vphone in i.items():
                if vphone == vFindFPhone:

                    print(vname, '->', vphone, ' - to rewrite input new info')

                    vCountItemForDel = vCountItem
                    break
        if vCountItemForDel >= 0:
            ContList.pop(vCountItemForDel)
            Name = input("Enter the Name: ")  # add try!
            phone = input("Enter the phone: ")  # add try!
            ni = {}
            ni.update({Name: phone})
            ContList.append(ni)
            with open(FunCOpener()[1], "wb") as varWordsFile:
                pickle.dump(ContList, varWordsFile)
    else:
        print("No recording to delete\n")
    if vCountItem < 1:
        print("Sorry but nothing delete\n")
    FunSubMenu1()
    return 3  # 0


def FunCreator(var_nsw: list):
    global ContList  # ?
    print("You must input Name, and Phone\n")
    Name = input("Enter the Name: ")  # add try!
    phone = input("Enter the phone: ")  # add try!
    ni = {}
    ni.update({Name: phone})
    ContList.append(ni)

    with open(var_nsw[1], "wb") as varWordsFile:
        pickle.dump(ContList, varWordsFile)
    return 1


def FunCOpener():
    MContactList = FunP1_tryOpenFile('ABook.txt')
    f = open(MContactList, 'rb')
    storedlist = pickle.load(f)  # загружаем объект из файла
    return [storedlist, 'ABook.txt']  # MContactList


def FunCensor(var_nsw=3, var_type=0):
    while var_nsw != 0:
        if var_type == 0:
            if var_nsw == 1:
                var_nsw = FunViewer()
            elif var_nsw == 2:
                var_nsw = FunCreator(FunCOpener())
            elif var_nsw == 4:
                #var_nsw = FunCreator(FunCOpener())
                var_nsw = FunSubMenu1()
                pass
            else:
                print("incorrectly input\nPlease try again (or 0 for exit):")
                var_nsw = FunCensor(FunCorrector1(var_nsw))
        elif var_type == 1:
            if var_nsw == 1:
                var_nsw = FunFindForName()
            elif var_nsw == 2:
                var_nsw = FunFindForPhone()
            elif var_nsw == 3:
                var_nsw = FunDelItem()
            elif var_nsw == 4:
                var_nsw = FunRewriteItem()
            elif var_nsw == 5:
                var_nsw = 1
                var_type = 0
            else:
                print("incorrectly input\nPlease try again (or 0 for exit):")
                var_nsw = FunCensor(FunCorrector1(var_nsw), 1)
        else:
            print("Undefined error - no type sbbmenu - exit...")
            var_nsw = 0
    else:
        sys.exit()


def FunMyMenu():
    print("Menu:\n1) View all list\n2) Addition new contact\n4) Options(subMenu)\n0) Exit\n")
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
