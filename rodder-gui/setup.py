#PLEASE NOTE: THIS FORMAT IS NOT REQUIRED TO SUBMIT TO THE MAIN REPO, NOR IS IT REQUIRED FOR RODDER TO FUNCTION. THIS IS ONLY A TEMPLATE, USABLE WITH MOST PROGRAMS
#Thanks, Drake.

import subprocess,requests,zipfile,os,shutil
dlurl = 'https://github.com/Ruthenic/rodder-gui/archive/master.zip' #this is where your download url 
print(">< Downloading rodder-gui...")
file = requests.get(dlurl)
with open(os.getenv('HOME') + '/.tmp/rodder/rodder-gui-master.zip', 'wb') as f: 
    f.write(file.content)
print(">< Extracting rodder-gui...")
with zipfile.ZipFile(os.getenv('HOME') + '/.tmp/rodder/rodder-gui-master.zip', 'r') as f:
    f.extractall(os.getenv('HOME') + '/.tmp/rodder')
print(">< Moving $PROGRAM_NAME to installation dir...")
shutil.move(os.getenv('HOME') + '/.tmp/rodder/rodder-gui-master', os.getenv('HOME') + '/.local/bin')
print(">< Adding $PROGRAM_NAME dir to $PATH")
with open(os.getenv('HOME') + '/.profile', 'a') as f:
    f.write('export PATH=' + os.getenv('HOME') + '/.local/bin/$EXTRACTED_FOLDER_NAME:$PATH #Created by rodder')
if 'fish' in subprocess.run('echo "$SHELL"', shell=True, capture_output=True).stdout.decode('utf-8').strip():
    subprocess.run('/usr/bin/fish -c "set -Ua fish_user_paths {}/.local/bin/rodder-gui-master"'.format(os.getenv('HOME')), shell=True)
print(">< Making rodder-gui executable...")
subprocess.run('chmod +x {}/.local/bin/rodder-gui-master/rodder-gui'.format(os.getenv('HOME')), shell=True)
print(">< Done!")
