from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of requirements.
    """
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '').strip() for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # type: ignore
        return requirements

setup(
    name='mlproject',
    version='0.1.0',
    author='Pankaj',
    author_email='pankajjsinghh376@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))

