import threading
from userHandler import UserHandler

miaUserName = 'qaqknn1mf4oa5ysh7c55rk8wt'
barelUserName = 'adwt3hr9ynmjt5cs3ahdcjg63'
cooperUserName = 'uwpq67zkbgeg7qxx2ya0y7mm9'

barel = UserHandler(barelUserName)
barel.start()

mia = UserHandler(miaUserName)
mia.start()

while mia.sortedGenres == [] or barel.sortedGenres == []:
    pass

print ('mia:')
print (mia.sortedGenres)
print('-_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_-')
print ('barel:')
print (barel.sortedGenres)