from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path: str) -> List[str]:
## find_packages() automatically finds all packages and subpackages
    """
    This function reads a requirements file and returns a list of requirements.
    """
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    # Remove any whitespace characters like `\n` at the end of each line
    requirements = [req.strip() for req in requirements if req.strip()]
    return requirements
setup(
    name='ml_project1',
    version='0.1.0',
    author='Sourav Raj',
    author_email="srvraj9135@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
        