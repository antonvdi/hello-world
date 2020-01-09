from cx_Freeze import setup, Executable

base = None    

executables = [Executable("basicgame.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Cobra",
    options = options,
    version = "1.0",
    description = 'Snake game with Python',
    executables = executables
)