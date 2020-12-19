import shutil,os
print(">< Deleting Firefox...")
shutil.rmtree(os.getenv('HOME') + '/.local/bin/$EXTRACTED_FOLDER_NAME')
print(">< Removing from path")
#with open(os.getenv('HOME') + '/.profile', ):
#TODO: remove path changing file from .profile
