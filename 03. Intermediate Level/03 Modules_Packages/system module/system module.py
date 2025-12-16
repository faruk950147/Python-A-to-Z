# ============================= What is System Module =============================
# System module is a module that provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import sys

# ============================= print argv =============================
print(f"Arguments =============================: {sys.argv}")

# ============================= check python version  =============================
print(f"Python version ===========================: {sys.version}")

# ============================= check python path  =============================
print(f"Python path ================================: {sys.path}")

# ============================= check python platform =============================
print(f"Python platform ============================: {sys.platform}")

# ============================= check python executable =============================
print(f"Python executable ============================: {sys.executable}")

# ============================= check python max size =============================
print(f"Python max size ==============================: {sys.maxsize}")


# ============================= loop =============================
for arg in sys.argv:
    print(arg)