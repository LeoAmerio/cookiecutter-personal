import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Intiializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

# Subproceso para instalar las librerias en requirements.txt
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

# Con conda
subprocess.call(['conda', 'env', 'create','--file','environment.yml'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun! {RESET_ALL}")