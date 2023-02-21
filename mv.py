import shutil

MOD_DATA_PATH = u'C:\\Users\\anton\\OneDrive\\Documents\\Proxy Studios\\Gladius\\Mods\\Adeptus\\Data'
DEV_MOD_PATH = u'C:\\Adeptus\\Mod\\Data'

try:
    shutil.rmtree(MOD_DATA_PATH)
except:
    pass
shutil.copytree(DEV_MOD_PATH, MOD_DATA_PATH)