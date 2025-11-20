
# 2 setuptools` is a Python library used to package and distribute Python projects.
# - **`setup()`** → main function that defines your package details
# - **`find_packages()`** → automatically finds all Python packages (folders containing `__init__.py`)
from setuptools import setup, find_packages
from typing import List

def get_requiements(file_path:str)->list[str]:#-> list[str] → function will return a list of strings
    """ this function will return the list of requirements 
    mentioned in the requirement.txt file
    """
    requiements=[]
    with open(file_path) as file_obj:
        requiements=file_obj.readlines()
        requiements=[req.replace("\n","") for req in requiements]
        if '-e .' in requiements:
            requiements.remove('-e .')
    return requiements
    
    # whenever we try to install requiement.txt at the time setup.py should run to buid the packkages so  it we provide -e. in requirement.txt it will automatically trigger set
    #-e. should not come here in the list of requiements so we will remove it

setup( name='Student Data Analysis',
    version='0.1.0',
    author='Samuel K C',
    author_email="samuelsam2k27@gmail.com",
    packages=find_packages(),# it will find all the packages in the source folder
    # install_requires=[
    #     'pandas','numpy','scikit-learn','flask','seaborn']
    install_requires=get_requiements('requirements.txt')
        )
# execute pip install -r requirement.txt
# it will automatically read all the requiements from requirement.txt and will install all the packages
