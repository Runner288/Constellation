# About __init__.py 
# __init__.py is a special file used to mark a directory as a Python package.
# It can be empty, or it can include initialization code that runs when the package is imported.

import libra.config as config 

if config.DEBUG == True :
    print(f"Running {__file__}")
    print(f"Debug: {config.DEBUG}")
    print("Importing Constellation Package")