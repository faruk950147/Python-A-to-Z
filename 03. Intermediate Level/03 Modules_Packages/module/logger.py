# # logger_module.py
# ========================= basic logger configuration =========================
# level is a parameter in basicConfig and it is optional
import logging
# it is basic configuration
# # Logger configuration
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler("app.log"),    # Log file
#         logging.StreamHandler()            # Console output
#     ]
# )

# # Shortcut functions
# def log_info(message):
#     logging.info(message)

# def log_error(message):
#     logging.error(message)

# def log_warning(message):
#     logging.warning(message)
    
# def log_debug(message):
#     logging.debug(message)


# ========================= advanced logger configuration =========================
# logger_module.py advanced configuration
#  difference between logging and logger and custom logger
# logging is a module
# logger is an object
# Custom logger
logger = logging.getLogger("AppLogger")
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Format set 
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Handlers add 
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Shortcut functions
def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)

def log_warning(message):
    logger.warning(message)
