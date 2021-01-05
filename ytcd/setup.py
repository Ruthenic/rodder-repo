#PLEASE NOTE: THIS FORMAT IS NOT REQUIRED TO SUBMIT TO THE MAIN REPO, NOR IS IT REQUIRED FOR RODDER TO FUNCTION. THIS IS ONLY A TEMPLATE, USABLE WITH MOST PROGRAMS
#Thanks, Drake.
import subprocess,requests,tarfile,os,shutil 
print(">< Downloading ytcd...")
subprocess.call('git clone https://github.com/Ruthenic/YoutubeChannelDownload ' + os.getenv('HOME') + '/.tmp/rodder/YoutubeChannelDownload', shell=True)
print(">< Moving ytcd to installation dir...")
shutil.move(os.getenv('HOME') + '/.tmp/rodder/YoutubeChannelDownload', os.getenv('HOME') + '/.local/bin')
print(">< Adding ytcd dir to $PATH")
with open(os.getenv('HOME') + '/.profile', 'a') as f:
    f.write('export PATH=' + os.getenv('HOME') + '/.local/bin/YoutubeChannelDownload:$PATH #Created by rodder')
subprocess.call('export PATH=' + os.getenv('HOME') + '/.local/bin/YoutubeChannelDownload:$PATH #Created by rodder', shell=True)
print(">< Setting ytcd as executable...")
subprocess.call('chmod a+x ' + os.getenv('HOME') + '/.local/bin/YoutubeChannelDownload/ytcd', shell=True)
print(">< Done!")
