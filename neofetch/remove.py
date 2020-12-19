import shutil,os
print(">< Deleting Firefox...")
shutil.rmtree(os.getenv('HOME') + '/.local/bin/dylanaraps-neofetch-60d07de')
print(">< Removing from path")
#with open(os.getenv('HOME') + '/.profile', ):
#TODO: remove path changing file from .profile
