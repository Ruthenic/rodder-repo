import subprocess,os,shutil
print(">< Checking for old install...")
if os.path.exists(os.getenv('HOME') + '/.config/rodder') == True or os.path.exists(os.getenv('HOME') + '/.local/rodder') == True:
    isDeleteOldInstall = 'y'
    if isDeleteOldInstall.lower() == 'y':
        shutil.rmtree(os.getenv('HOME') + '/.local/rodder')
        #shutil.rmtree(os.getenv('HOME') + '/.config/rodder')
        #shutil.rmtree(os.getenv('HOME') + '/.tmp/rodder')
    else:
        print(">< Cannot continue. Exiting :(...")
        exit()
isUserInstall = 'y'
print(">< Cloning rodder git repo...")
print(subprocess.check_output('git clone https://github.com/ruthenic/rodder ' + os.getenv('HOME') + '/.tmp/rodder', shell=True))
print(">< Moving to installation directory...")
if isUserInstall.lower() == "y" or isUserInstall.lower() == "":
    path = '~/.local/rodder'
    shutil.move(os.getenv('HOME') + '/.tmp/rodder', os.getenv('HOME') + '/.local')
elif isUserInstall.lower() == "n":
    path = '/usr/local/rodder'
    print("Input your password to install to root (WARNING: NOT FULLY FUNCTIONAL, NOR FULLY TESTED.).")
    subprocess.call('sudo mv ~/.tmp/rodder /usr/local', shell=True)
else:
    print("Error: invalid selection! Exiting...")
    exit()
#shutil.rmtree(os.getenv('HOME') + '/.tmp/rodder')
subprocess.call('export PATH=' + os.getenv('HOME') + '/.local/rodder:$PATH', shell=True)
print(">< Done updating rodder!")
