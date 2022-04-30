from os import listdir, getcwd, system, getlogin
from os.path import isfile, join, getmtime, splitext
from datetime import datetime

# Función para comprobar si el nombre del archivo ya tiene la fecha incluida
def TieneFecha(str):

    str = str[-14::]
    if str[0] == "_" and str[9] == "_":

        try:
            _ = int(str[1:8])
            _ = int(str[10:14])
            return True
            
        except ValueError:
            return False
    else:
        return False

user = (getlogin())
user = "RDO"

extensions = [".7z",
              ".zap13",
              ".zap14",
              ".zap15",
              ",zap15_1",
              ".zap16",
              ".zip",
              ".rar"]

cwd = getcwd()

if not "OLD" in listdir(cwd):
    system("mkdir OLD")

files = [f for f in listdir(cwd) if isfile(join(cwd, f))]


for file in files:
    
    name, extension = (splitext(file))

    if extension in extensions:
        
        if not TieneFecha(name):
            date = (getmtime(file))
            date = datetime.utcfromtimestamp(date).strftime('%Y%m%d_%H%M')
            new_file = 'OLD\\'+name + "_" + date + extension
        else:
            new_file = 'OLD\\'+name + extension
            
        cmd = " ".join(('move', join(cwd,file), join(cwd,new_file)))
        system(cmd)
