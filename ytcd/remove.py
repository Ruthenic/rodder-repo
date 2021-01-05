import shutil,os
print(">< Deleting ytcd...")
shutil.rmtree(os.getenv('HOME') + '/.local/bin/YoutubeChannelDownload')
print(">< Removing from path")
#with open(os.getenv('HOME') + '/.profile', ):
#TODO: remove path changing file from .profile
