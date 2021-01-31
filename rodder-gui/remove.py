import shutil,os
print(">< Deleting rodder-gui...")
shutil.rmtree(os.getenv('HOME') + '/.local/bin/rodder-gui-master')
print(">< Removing from path")
#with open(os.getenv('HOME') + '/.profile', ):
#TODO: remove path changing file from .profile
