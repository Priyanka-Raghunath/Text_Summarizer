# PROJECT TEMPLATE CREATION

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name='textSummarizer'

list_of_files=[
    '.github/workflows/.gitkeep' # CI/CD related yaml files are written here for AWS deployement(for which github is required)
    # at the time of commit at github, the changes is also directed to the cloud(aws)
    #.gitkeep is just a dummy file, which will be replaced with yaml file later
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init.py',
    f'src/{project_name}/utils/__init.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging//__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile', # Docker image of the source code is made which is deployed in AWS
    'requirements.txt',
    'setup.py',
    'research/trails.ipynb'
]

# Creating files and folders

# in windows we use backward slash in path whereas in linux, we use forward
# handle them carefully(use Path library)
for filepath in list_of_files:
    filepath=Path(filepath) # gives path based on operating system used

    # separate folders and files
    filedir, filename=os.path.split(filepath)
    
    # check if file directory is empty
    if filedir != '':
        os.makedirs(filedir,exist_ok=True) # exist_ok=True ensures that new directory is not made if it already exists
        logging.info(f'Creating directory: {filedir} for the file {filename}') # displays information at the terminal
    
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Creating empty file: {filepath}')

    else:
        logging.info(f'The file {filepath} already exists')
        