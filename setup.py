from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='get_hubway_data',  # Required
    version='0.1',  # Required
    description='Extract data from Hubway CSVs',  # Required
    long_description=long_description,  # Optional
    url='https://github.com/Gvanderl/Neurala',  # Optional
    py_modules=["get_hubway_data"],
    install_requires=['matplotlib', 'pandas']
)
