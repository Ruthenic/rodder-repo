import subprocess,requests,zipfile,os,shutil
dlurl = 'https://api.github.com/repos/dylanaraps/neofetch/zipball/7.1.0'
print(">< Downloading Neofetch...")
file = requests.get(dlurl)
with open(os.getenv('HOME') + '/.tmp/rodder/dylanaraps-neofetch-7.1.0-0-g60d07de.zip', 'wb') as f:
    f.write(file.content)
print(">< Extracting Neofetch...")
with zipfile.ZipFile(os.getenv('HOME') + '/.tmp/rodder/dylanaraps-neofetch-7.1.0-0-g60d07de.zip') as f:
    f.extractall(os.getenv('HOME') + '/.tmp/rodder')
print(">< Moving Neofetch to installation dir...")
shutil.move(os.getenv('HOME') + '/.tmp/rodder/dylanaraps-neofetch-60d07de', os.getenv('HOME') + '/.local/bin')
print(">< Adding Neofetch dir to $PATH")
with open(os.getenv('HOME') + '/.profile', 'a') as f:
    subprocess.call('export PATH=' + os.getenv('HOME') + '/.local/bin/dylanaraps-neofetch-60d07de:$PATH', shell=True)
    f.write('export PATH=' + os.getenv('HOME') + '/.local/bin/dylanaraps-neofetch-60d07de:$PATH #Created by rodder')
print(">< Marking neofetch as executable...")
subprocess.call('chmod +x ' + os.getenv('HOME') + '/.local/bin/dylanaraps-neofetch-60d07de/neofetch', shell=True)
print(">< Done!")
