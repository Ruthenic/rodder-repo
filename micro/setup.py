import subprocess,os,shutil
print(">< Making micro directory...")
try:
    os.makedirs(os.getenv('HOME') + '/.local/bin/micro')
except:
    shutil.rmtree(os.getenv('HOME') + '/.local/bin/micro')
    os.makedirs(os.getenv('HOME') + '/.local/bin/micro')
print(">< Downloading and running micro install script...")
subprocess.run('cd '+ os.getenv('HOME') + '/.local/bin/micro && ' +  'curl https://getmic.ro | bash', shell=True)
subprocess.run('export PATH=' + os.getenv('HOME') + '/.local/bin/micro:$PATH', shell=True)
