#!/usr/bin/env python3
#rename script by Chrisstring,
#updated the folder names for consistency
#added all names to lowercase 5/17

#Please see copyFilesSample.csv for an example of how the CSV file needs to be constructed!

import os, csv, shutil

def renameFunction(sinput,soutput):
    for fileName in fileList:
        if fileName.startswith(sinput):
            os.rename(fileName,fileName.replace(sinput,soutput).lower().replace('_','-'))
            #shutil.copy2(fileName,os.path.join(inputPath,fileName.replace(sinput,soutput))) #old COPY utility
            print("{} was found\trenamed to {}".format(fileName,fileName.replace(sinput,soutput).lower().replace('_','-')))



print("Welcome to the SUPER RENAME Number 1")
print("This utility RENAMES files in place!, so make a copy of the files ahead of time!")
inputPath = input("PATH to Folder root containing files (dragging is okay):").strip().replace('\\', '')
#if os.path.isdir(os.path.join(inputPath,"_renamed")):
#    pass
#else:
#    os.makedirs(os.path.join(inputPath,"_renamed"))

#makedir if it doesn't exist

print()
print()
print("=========== CSV MUST HAVE FIRST COLUMN IS INPUT name, SECOND COLUMN IS OUTPUT name============")
csvPath = input("DRAG your CSV here:").strip().replace('\\', '')

fileList = os.listdir(inputPath)
os.chdir(inputPath)

#remove directories
for fileName in fileList:
        if os.path.isdir(os.path.join(inputPath,fileName)):
            fileList.remove(fileName)
            print("found a directory, removed it from csv master list: ",fileName)

#open csvreader
csvReader = csv.reader(open(csvPath,newline=''),delimiter=',')
for row in csvReader:
    renameFunction(row[0],row[1])



#items removed
#print("This is the fileList")
#print("searching for T534062")
#change to the directory
