import sys
import platform

# Check Python implementation
print(f"Using sys implementation: {sys.implementation}")
print(f"Using platform implementation: {platform.python_implementation()}")

# Check Python version
print(f"Using sys version: {sys.version}")
print(f"Using platform version: {platform.python_version()}")

# Check Python path
print(f"Using sys path: {sys.path}")
print(f"Using sys executable: {sys.executable}")  # optional: Python interpreter path
