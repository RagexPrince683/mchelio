import os

def appendDamageFactor(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        # Only process files (not subdirectories)
        if os.path.isfile(file_path):
            with open(file_path, 'a') as f:
                f.write("DamageFactor = 0.8")


appendDamageFactor(os.getcwd())
DamageFactor = 0.8