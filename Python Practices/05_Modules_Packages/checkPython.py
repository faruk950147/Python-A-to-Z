# how to check cpython or other python implementation
import sys
import platform

print(f"Using sys implementation: {sys.implementation}")
print(f"Using platform implementation: {platform.python_implementation()}")

# how to check python version
print(f"Using sys version: {sys.version}")
print(f"Using platform version: {platform.python_version()}")

# how to check python path
print(f"Using sys path: {sys.path}")
print(f"Using platform path: {platform.python_path()}")
