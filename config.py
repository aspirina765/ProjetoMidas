#!/usr/bin/env python
import threading
import os

# def background_setup():
#     # Explicitly importing this from the context of the child thread
#     from config import settings
#     settings.setup()
#     print(settings.ROOT_DIR)

def background_setup():
    from config import settings
    settings.setup()
    curd = settings.ROOT_DIR
    return curd #+ '/'

dataDir = background_setup().rsplit(os.sep,1)[0] + '/data/GoogleDrive/'
print(dataDir)

os.environ['dataDir'] = dataDir
cmd = "dotenv set dataDir {var}".format(var=dataDir)
os.system(cmd)

print(os.environ['dataDir'])




# Spawn a thread to background preparation tasks
# t = threading.Thread(target=background_setup)
# t.start()
#
# # Do other things during initialization
#
# t.join()
#
# # Ready to take traffic