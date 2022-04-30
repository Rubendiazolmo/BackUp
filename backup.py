from os import listdir, getcwd, system, getlogin
from os.path import isfile, join, getmtime, splitext
from datetime import datetime

user = (getlogin())

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
        
        date = (getmtime(file))
        date = datetime.utcfromtimestamp(date).strftime('%Y%m%d_%H%M')
        new_file = 'OLD\\'+name + "_" + date + extension
        cmd = " ".join(('move', join(cwd,file), join(cwd,new_file)))
        system(cmd)
