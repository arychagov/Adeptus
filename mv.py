import shutil

STABLE_MOD_DATA_PATH = u'C:\\Users\\anton\\OneDrive\\Documents\\Proxy Studios\\Gladius\\Mods\\Adeptus\\Data'
BETA_MOD_DATA_PATH = u'C:\\Users\\anton\\OneDrive\\Documents\\Proxy Studios\\Gladius\\Mods\\Adeptus Beta\\Data'
DEV_MOD_PATH = u'C:\\Adeptus\\Mod\\Data'

def delete_and_copy(mod_path):
    try:
        shutil.rmtree(mod_path)
        shutil.copytree(DEV_MOD_PATH, mod_path)
    except:
        pass

delete_and_copy(STABLE_MOD_DATA_PATH)
delete_and_copy(BETA_MOD_DATA_PATH)