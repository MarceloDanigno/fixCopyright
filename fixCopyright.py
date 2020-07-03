#encoding=utf-8
import os
import sys
import re
import glob

if len(sys.argv) < 3:
    print("Usage: " + sys.argv[0] + " <path to check> <0=TCL, 1=C++, 2=ALLfiles> <recursiveTrue?>")
    exit()

path = sys.argv[1]
filesToCheck = int(sys.argv[2])
recursiveFlag = False
if int(sys.argv[3]) != 0:
    recursiveFlag = True


tclBlock = open("tcl_copyright_block.txt", "r")
tclBlockText = tclBlock.read().split("\n")
tclBlock.close()

cppBlock = open("cpp_copyright_block.txt", "r")
cppBlockText = cppBlock.read().split("\n")
cppBlock.close()

if (len(path) > 1):
    os.chdir(path)

tclFiles = []
cppFiles = []

if (filesToCheck == 0 or filesToCheck == 2):
    tclFiles = tclFiles + glob.glob('./**/*.tcl', recursive=recursiveFlag)

if (filesToCheck == 1 or filesToCheck == 2):
    cppFiles = cppFiles + glob.glob('./**/*.cpp', recursive=recursiveFlag)
    cppFiles = cppFiles + glob.glob('./**/*.h', recursive=recursiveFlag)
    cppFiles = cppFiles + glob.glob('./**/*.cc', recursive=recursiveFlag)
    cppFiles = cppFiles + glob.glob('./**/*.hh', recursive=recursiveFlag)

allFiles = tclFiles + cppFiles

print("Files to check: " + str(len(allFiles)) + ".")

for fileTextData in allFiles:
    f = open(fileTextData, "r", encoding="utf8", errors='ignore')
    textData = f.read().split("\n")
    lineCounter = 0
    startLine = 0
    endLine = 0
    foundStart = False
    foundEnd = False
    commentsStart = False
    isCpp = False
    if fileTextData in cppFiles:
        isCpp = True
    while lineCounter < len(textData):
        line = textData[lineCounter]
        line = line.replace(" ","")
        if isCpp == True:
            if "//" not in line and line != "":
                break
        else:
            if "#" not in line and line != "":
                break
        line = line.replace("#","")
        line = line.replace("/","")
        line = line.replace("*","")
        if line == "":
            if commentsStart == False:
                startLine = lineCounter
                commentsStart = True
            if foundEnd == True and commentsStart == True:
                endLine = lineCounter
        else:
            if "BSD" in line:
                foundStart = True
                if commentsStart == False:
                    startLine = lineCounter
                    commentsStart = True
            else: 
                if "DAMAGE." in line and foundStart == True:
                    foundEnd = True
                    endLine = lineCounter
        lineCounter += 1
    f.close()
    f = open(fileTextData, "w", encoding="utf8", errors='ignore')
    exportText = []
    if foundStart and foundEnd:
        del textData[startLine:endLine]
        if isCpp == True:
            exportText = textData[0:startLine] + cppBlockText + textData[startLine:len(textData)]
        else:
            exportText = textData[0:startLine] + tclBlockText + textData[startLine:len(textData)]
    else:
        if isCpp == True:
            exportText = cppBlockText + textData
        else:
            exportText = tclBlockText + textData
    exportText = "\n".join(exportText)
    f.write(exportText)
    f.close()

print("Copyright fixed!")
