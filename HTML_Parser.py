import urllib.request
import webbrowser
import sys
import re

url = sys.argv[1]
tmp = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

site = urllib.request.urlopen(tmp)
data = site.read()

print(data)
fileName = "file.txt"
parsedFileName = "file1.html"

file = open(fileName,"wb")
file.write(data)
file.close()

f = open(fileName,encoding='utf8')

lineList = f.readlines()

fileTmp = open(parsedFileName,"w",encoding='utf8')

for val in lineList:
    sss = re.sub(r'\s?styl\w+="[^"]+"\s?', '', val)
    fileTmp.write("%s" % sss)

fileTmp.close()

webbrowser.open(parsedFileName)
