#import os
#       FILE DETECTION
#path = "C:\\Users\\Guilherme Vieira\\Desktop\\textopy.txt"

#if os.path.exists(path):
#    print("That location exists!")
#    if os.path.isfile(path):
#        print("That is a file")  #diferenciar se é um arquivo(caso seja uma pasta ele n confirmará)
#    elif os.path.isdir(path):
#        print("That is a directory")
#else:
#    print("That location doesn't exist!")


#        LER UMA FILE
#try:
#    with open("C:\\Users\\Guilherme Vieira\\Desktop\\textopy.txt") as file:  # with open fecha o arquivo automaticamente
#        print(file.read())
#
#except FileNotFoundError:
#    print("That file was not found!")  # caso não ache o arquivo.

#       ESCREVER UMA FILE

#text = "Have a Nice Day Cuuh!"

#with open("C:\\Users\\Guilherme Vieira\\Desktop\\textopy.txt", 'a') as file:
#    file.write(text)

#       COPIAR UMA FILE

#   copyfile() = copies contents of a FILE
#   copy() = copyfile() + permission mode + destination can be a directory
#   copy2() = copy() + copies metadata (file's creation and modification times)

#import shutil

#shutil.copyfile("C:\\Users\\Guilherme Vieira\\Desktop\\textopy.txt", 'copy.txt') #source,destination

#       MOVE A FILE

#import os

#source = "copy.txt"
#destination = "C:\\Users\\Guilherme Vieira\\Desktop\\test.txt"

#try:
#    if os.path.exists(destination):
#        print("There is already a file there")
#    else:
#        os.replace(source,destination)
#        print(source+" was moved")
#except FileNotFoundError:
#    print(source+" was not found")

#       DELETE A FILE

import os
import shutil

path = 'folder'

try:
      os.remove(path)       # DELETA A FILE
    # os.rmdir(path)        # DELETA O DIRETORIO VAZIO
    # shutil.rmtree(path)   # FUNÇÃO PERIGOSA POIS REMOVE A PASTA JUNTO COM TODOS OS FILES NELA INSERIDOS!
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You dont have permission to delete that")
except OSError:
    print("The folder is not empty")
else:
    print(path+" was deleted")