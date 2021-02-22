import subprocess,requests,zipfile,os,shutil
dlurl = 'https://github.com/Ruthenic/rodder-gui/archive/master.zip' #this is where your download url 
print(">< Downloading rodder-gui...")
file = requests.get(dlurl)
with open(os.getenv('HOME') + '/.tmp/rodder/rodder-gui-master.zip', 'wb') as f: 
    f.write(file.content)
print(">< Extracting rodder-gui...")
with zipfile.ZipFile(os.getenv('HOME') + '/.tmp/rodder/rodder-gui-master.zip', 'r') as f:
    f.extractall(os.getenv('HOME') + '/.tmp/rodder')
print(">< Moving rodder-gui to installation dir...")
shutil.move(os.getenv('HOME') + '/.tmp/rodder/rodder-gui-master', os.getenv('HOME') + '/.local/bin')
print(">< Adding rodder-gui dir to $PATH")
with open(os.getenv('HOME') + '/.bashrc', 'a') as f:
    f.write('export PATH=' + os.getenv('HOME') + '/.local/bin/rodder-gui-master:$PATH #Created by rodder')
if 'fish' in subprocess.run('echo "$SHELL"', shell=True, capture_output=True).stdout.decode('utf-8').strip():
    subprocess.run('/usr/bin/fish -c "set -Ua fish_user_paths {}/.local/bin/rodder-gui-master"'.format(os.getenv('HOME')), shell=True)
print(">< Making rodder-gui executable...")
subprocess.run('chmod +x {}/.local/bin/rodder-gui-master/rodder-gui'.format(os.getenv('HOME')), shell=True)
print(">< Installing dependencies...")
subprocess.run('python3 -m pip install -r {}/.local/bin/rodder-gui-master/requirements.txt'.format(os.getenv('HOME')), shell=True)
print(">< Done!")
