#!  ~/Desktop/Untils/Python
#   Author: FTd
#   Date: 2014/01/17
#   Description: cature the download link

filename = "C:\Users\dell\Desktop\Untils\Python\ShowFile.txt"
lines = []
try:
    f = open(filename, 'r')
    lines = f.readlines()
except IOError as e:
    print e
else:
    for line in lines:
       print line 
finally:
    f.close()
