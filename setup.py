from setuptools import setup,find_packages

setup(
    name='wild_requests',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/taux1c/wild_requests',
    author='Taux1c',
    install_requires=['httpx~=0.25.0'],
    description='Just a module that provides some tools for downloading.',
)
