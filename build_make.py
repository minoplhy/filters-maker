import os
import glob
import shutil

def filepath_mass_changer(Version ,path ,apapath):
    f = glob.glob(os.path.join(path,"*.txt"))
    for filename in f:
        s = os.path.basename(filename)
        os.rename(filename, os.path.join(path, Version + '_' + s ))
    shutil.copytree(path, apapath)