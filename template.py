import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Basic file directory for modular coding
list_of_files = [
    "src/__init__.py", # Helps to import functions 
    "src/helper.py", # To keep store functions 
    ".env", # Use to store variables
    "setup.py", # For package building
    "research/trials.ipynb", # Shift your run.ipynb here
    "app.py", # Flask application
    "static/style.css", # CSS file
    "templates/index.html" # HTML file
]

# Path will get to know which os it is    
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Ensure the directory exists before proceeding
    if filedir!= '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory '{filedir}' created for the file '{filename}'.")
    else:
        logging.warning("Skipping creation of file/directory due to invalid path.")

    # Check if the file exists and is not empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already created.")