# ======================= what is python script =======================
# Python script is a file that contains python code
import sys
print("Hello World")

# ============================= run python script =============================
# command to run python Directly as a script:
# This runs the Python file directly.
# Use this for standalone scripts.
# python main.py

# ============================= run python script =============================
# command to run python Using the -m module flag:
# This runs the file as a module.
# Useful when the file is part of a package or you want module-relative imports to work.
# without extension .py execute 
# python -m main

# specific library specific directory
# python -m pip install requests --target=/path/to/directory
# python -m pip install requests --target .

# ============================= what is pythonpath =============================
# Pythonpath is a refers to a list of directories that
# Python will search for modules to import.
# and other files when executing a script. or importing a module

# print(sys.path)
# python command line
# where python # show python path
# python -c "import sys; print(sys.path)" # show python path
# python -m pip install requests
# python -m pip install requests --target=/path/to/directory
# python -m pip install requests --target .
# python file name.py # run python file or script
# python -m file name.py # run python file or script

