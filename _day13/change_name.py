# 1) stworz katalog `animals`
# 2) stworz puste pliki w tym katalogu z nazwami podanymi w zmiennej `files`
# 3) po stworzeniu wszystkich plików zmień ich nazwy tak by dodać do nich index
#      np: 01_koty, 02_psy
import os,sys,shutil
os.mkdir('animals')
files = ['koty', 'psy', 'kangury', 'pandy', 'leopardy', 'orki', 'walenie']
for i in files:
    open(os.path.join('animals', i), 'a').close()



for i,j in enumerate(files):
    os.rename('animals/'+j, 'animals/'+ '0' + str(i) + '_' + j)
    

x = input('created and renamed animals, remove? [1] - yes [0] - no')
if int(x) == 1:
    shutil.rmtree('animals')
    
