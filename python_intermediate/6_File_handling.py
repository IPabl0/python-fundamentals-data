### File handling ###
import os

#need *.txt file

txt_file = open ("Intermedio/my_file.txt", "r+")
#print (txt_file.read())
#print (txt_file.readline())
#print (txt_file.readline())
#print (txt_file.readlines())

for line in  txt_file.readlines():
    print (line)