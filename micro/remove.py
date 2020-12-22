import shutil,os
print(">< Deleting micro...")
try:
    shutil.rmtree(os.getenv('HOME') + '/.local/bin/micro')
except:
    print("ERROR: Installation directory not found! Exiting...")
print(">< Removing from path")
#with open(os.getenv('HOME') + '/.profile', ):
#TODO: remove path changing file from .profile
