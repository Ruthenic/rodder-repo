#PLEASE NOTE: THIS FORMAT IS NOT REQUIRED TO SUBMIT TO THE MAIN REPO, NOR IS IT REQUIRED FOR RODDER TO FUNCTION. THIS IS ONLY A TEMPLATE, USABLE WITH MOST PROGRAMS
#Thanks, Drake.

import subprocess,requests,tarfile,os,shutil
dlurl = '$DOWNLOAD_LINK' #this is where your download url 
print(">< Downloading $PROGRAM_NAME...")
file = requests.get(dlurl)
with open(os.getenv('HOME') + '/.tmp/rodder/$DOWNLOADED_FILE', 'wb') as f: 
    f.write(file.content)
print(">< Extracting $PROGRAM_NAME...")
with tarfile.open(os.getenv('HOME') + '/.tmp/rodder/$DOWNLOADED_FILE', 'r') as f:
    f.extractall(os.getenv('HOME') + '/.tmp/rodder')
print(">< Moving $PROGRAM_NAME to installation dir...")
shutil.move(os.getenv('HOME') + '/.tmp/rodder/$EXTRACTED_FOLDER_NAME', os.getenv('HOME') + '/.local/bin')
print(">< Adding $PROGRAM_NAME dir to $PATH")
with open(os.getenv('HOME') + '/.profile', 'a') as f:
    f.write('export PATH=' + os.getenv('HOME') + '/.local/bin/$EXTRACTED_FOLDER_NAME:$PATH #Created by rodder')
print(">< Done!")
