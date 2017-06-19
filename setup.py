from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zerotier',
    version='1.1.1',
    description='Zerotier API client',
    long_description=long_description,
    url='https://github.com/zero-os/zerotier_client',
    author='GIG',
    author_email='info@gig.tech',
    license='Apache 2.0',
    packages=find_packages(),
    install_requires=['requests'],
)
