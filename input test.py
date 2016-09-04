import os, shutil

def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]

def File_Transfer():

    source = input ('Start folder? ')
    folder = os.listdir(source)
    newFolder = input ('New Folder? ')
    fileName = input ('New File Name: ')
    extn = input ('File extension: ')

    S = []
    for L in folder:
        S.append(L)
    bubble(S)

    n = 1
    for i in S:
        if n < 10:
            name = fileName[:-1]+str(n) + '.' + str(extn)
        else:
            name = fileName[:-2]+str(n) + '.' + str(extn)

        shutil.copy (str(source) + '\\' + str(i), newFolder + '\\' + name)
        n += 1


File_Transfer()
