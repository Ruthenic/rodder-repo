import subprocess,requests,tarfile,os,shutil
dlurl = 'https://download-installer.cdn.mozilla.net/pub/firefox/releases/84.0/linux-x86_64/en-US/firefox-84.0.tar.bz2'
print(">< Downloading Firefox...")
file = requests.get(dlurl)
with open(os.getenv('HOME') + '/.tmp/rodder/firefox.tar.bz2', 'wb') as f:
    f.write(file.content)
print(">< Extracting Firefox...")
with tarfile.open(os.getenv('HOME') + '/.tmp/rodder/firefox.tar.bz2', 'r:bz2') as f:
    f.extractall(os.getenv('HOME') + '/.tmp/rodder')
print(">< Moving Firefox to installation dir...")
shutil.move(os.getenv('HOME') + '/.tmp/rodder/firefox', os.getenv('HOME') + '/.local/bin')
print(">< Adding Firefox dir to $PATH")
with open(os.getenv('HOME') + '/.profile', 'a') as f:
    f.write('export PATH=' + os.getenv('HOME') + '/.local/bin/firefox:$PATH #Created by rodder')
print(">< Done!")
