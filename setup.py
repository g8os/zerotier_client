from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open('README.md') as f:
    readme = f.read()

setup(
    name='zerotier',
    version='1.1.2',
    description='Zerotier API client',
    long_description=readme,
    url='https://github.com/zero-os/zerotier_client',
    author='GIG',
    author_email='info@gig.tech',
    license='Apache 2.0',
    packages=find_packages(),
    install_requires=['requests'],
)
