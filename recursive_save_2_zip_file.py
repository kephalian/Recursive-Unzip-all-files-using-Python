#import shutil
from zipfile import ZipFile
import PySimpleGUI as sg
import os, glob, sys
#from PyPDF2 import PdfFileMerger

sg.theme("material1")
#os.chdir('/storage/emulated/0')
files_ = []
for file in glob.glob("**/*",recursive=True):
    if os.path.isfile(file):files_.append(file)
  
if files_ is None: sys.exit()   
sg.popup_scrolled(files_, title='List of files' , size=(125,25))

# Full path of
# the archive file
#filename = "/home/User/Downloads/file.zip"
 
# Target directory
#extract_dir = "/home/ihritik/Documents"
 
# Format of archive file
archive_format = "zip"
 
# Unpack the archive file



file=sg.popup_get_text('Enter name of Archieve to create', default_text='backup.zip')

if file is None: sys.exit()
file=os.path.basename(file)+'.zip'
with ZipFile(file, 'w') as zip2:
    for i in files_:
        if sg.popup_yes_no(f"Add this file to archieve {i}", title='Add this to zip file')=='No':continue
        zip2.write(i)
zip2=ZipFile(file)      
check1=zip2.testzip()
if check1 is None:
    sg.popup(f'Tested contents of {file} No errors', title='Success')
else:
    sg.popup(f'Tested contents of {file} Error found in {check1}', title='Bad zip')


