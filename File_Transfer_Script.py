import shutil, os

def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]


source1 = os.chdir ('D:\\UTorrent\[AliQ] Girl Meets World Season 2 [1080p;WEB-DL x264]')
source= ('D:\\UTorrent\[AliQ] Girl Meets World Season 2 [1080p;WEB-DL x264]')
newloc = ('D:\\TV\Girl Meets World\Girl Meets World S02')

F = os.listdir(source1)
S = []

for L in F:
    S.append(L)

bubble(S)

n = 17
for i in S:
    if n<10:
        name = 'Girl Meets World S02E0'+str(n)+'.mp4'
    else:
        name = 'Girl Meets World S02E'+str(n)+'.mp4'
    shutil.copy (str(source) + '\\' + str(i), newloc +'\\' + name)
    os.unlink(source + '\\' + i)
    print ('file' + str(n))
    n+=1
