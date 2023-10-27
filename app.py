import os
import shutil
path=input("enter your path :")
files=os.listdir(path)

for i in files:
    filename,extension=os.path.splitext(i)
    ext=extension[1:]
    folder_path=path+"\\"+ext
    if os.path.exists(folder_path):
        shutil.move(path+"\\"+i,path+"\\"+ext+"\\"+i)
    else :
        os.makedirs(folder_path)
        shutil.move(path+"\\"+i,path+"\\"+ext+"\\"+i)