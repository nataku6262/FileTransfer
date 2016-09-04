import os

def listDir():
    someList=[]
    folder = os.listdir(input('Directory here'))

    for F in folder:
        someList.append(F)
    print (someList[0])
    #return someList[0]

listDir()
